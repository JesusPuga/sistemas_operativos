import BDConexion
from BDConexion import *
import os
from loadStudents import *
from datetime import *

con = Conexion(os.environ['USER_SISTEMAS'],
               os.environ['PASSWORD_SISTEMAS'],
               "FacultadBD")

"""Retorna True si es posible continuar inscribiendo
       False en caso contrario
"""
def validateInscriptionHour(carnetAlumno):
    query = """SELECT Inscripcion.fechaInscripcion
               FROM Inscripcion
               INNER JOIN Alumno
                     ON Alumno.claveInscripcion = Inscripcion.claveInscripcion AND
                        Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(carnetAlumno,), True)

    for inscriptionDate in result:
        if inscriptionDate[0] + timedelta(hours = 2) > datetime.now() or inscriptionDate[0]  < datetime.now() :
            print(inscriptionDate[0])
            return False

    return True

"""
    Verifica si la materia depende de aprobar algún otra
        -Retorna False en caso de no requrir aprobar alguna materia
        -Retorna un String con el nombre de la materia que necesita pasar
            +String se toma como True en una validación
"""
def isRequiredSubject(subjectClave, studentClave):
    findSubject = """SELECT Materia.claveMateria
                     FROM Materia
                     INNER JOIN Oportunidad
                     ON Oportunidad.claveMateria = %s AND
                        Oportunidad.calificacion >= 70 AND
                        Oportunidad.carnetAlumno = %s
                  """

    findPreviousSubjectId = """SELECT Materia_Seriada.claveMateria
                             FROM Materia_Seriada
                             WHERE claveMateriaSeriada = %s
                          """

    previousSubject = con.execute_query(findPreviousSubjectId,(subjectClave,),True).fetchone()

    if previousSubject != None:
        subject = con.execute_query(findSubject,(previousSubject[0], studentClave),True).fetchone()
        #¿No ha pasado la materia?
        if subject == None:
            findPreviousSubjectInf = """SELECT nombre
                                        FROM Materia
                                        WHERE claveMateria = %s
                                     """
            subjectInf = con.execute_query(findPreviousSubjectInf,(previousSubject[0],),True).fetchone()

            return subjectInf[0] #python toma una String comoo True

    return False

"""
    Verifica si el horario del grupo se empalma con algún otro
        -Retorna Materia empalmada en caso de que se empalme
        -Retorna False en caso contrario
"""
def isScheduleUsed(groupClave,studentClave, subjectClave,period= "2018-01-16"):
    query = """
            SELECT Materia.nombre,Dia_Horario.IDDia,Horario.horaInicio, Horario.HoraFin
            FROM Alumno_Grupo
            INNER JOIN Grupo ON Alumno_Grupo.claveGrupo = Grupo.claveGrupo = %s  AND
                                Alumno_Grupo.carnetAlumno = %s AND
                                Grupo.periodo = %s AND
                                Grupo.claveMateria = %s
            INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria
            INNER JOIN Horario ON Horario.claveGrupo = Grupo.claveGrupo
            INNER JOIN Dia_Horario  ON Dia_Horario.IDHorario = Horario.IDHorario;
            """
    result = con.execute_query(query, (groupClave,studentClave, period, subjectClave), True)

    for nombre, claveDia, startHour, finishHour in result:

        query = """
                    SELECT Dia_Horario.IDDia, Materia.nombre,Horario.horaInicio, Horario.HoraFin
                    FROM Alumno_Grupo
                    INNER JOIN Grupo ON Alumno_Grupo.claveGrupo = Grupo.claveGrupo  AND
                                        Alumno_Grupo.carnetAlumno = %s AND
                                        Grupo.periodo = %s
                    INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria
                    INNER JOIN Horario ON Horario.claveGrupo = Grupo.claveGrupo AND
                                            ((Horario.horaInicio >= %s AND
                                              Horario.horaInicio < %s) OR
                                             (Horario.horaFin > %s AND
                                              Horario.horaFin <= %s))
                    INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario AND
                                              Dia_Horario.IDDia = %s;
                """
        result = con.execute_query(query, (studentClave,period,startHour,finishHour,startHour,finishHour,claveDia), True)
        schedulesFound = result.fetchone()

        if schedulesFound != None:
            return  schedulesFound

    return False

"""
    Retorna cantidad de alumnos inscritos en una materia
"""
def checkCounterInGroup(groupClave, subjectClave, periodo = "2018-01-16"):
    query = """SELECT contador
               FROM Grupo
               WHERE claveGrupo = %s AND claveMateria = %s AND periodo = %s
            """
    result = con.execute_query(query, (groupClave, subjectClave,periodo), True)

    return result.fetchone()[0]
"""
    Retorna la capacidad del grupo dependiendo la materia y el periodo
"""
def checkCapacityInGroup(groupClave, subjectClave, periodo = "2018-01-16"):
    query = """
                SELECT capacidad
                FROM Grupo
                WHERE claveGrupo = %s AND claveMateria = %s AND periodo = %s
            """
    result = con.execute_query(query, (groupClave, subjectClave,periodo), True)

    return result.fetchone()[0]
"""
    Actualiza contador en grupo
"""
def updateGroupCounter(counter,groupClave, subjectClave, periodo = "2018-01-16"):
    query = """UPDATE Grupo SET contador = %s
               WHERE claveGrupo = %s AND claveMateria = %s AND periodo = %s;
            """

    con.execute_query(query, (counter + 1,groupClave, subjectClave,periodo), False, True)

"""
    Retorna la oportunidad actual de una materia dependiendo el alumno
"""
def findSubjectOportunity(studentClave,subjectClave):
    query = """SELECT numOportunidad
               FROM Oportunidad
               WHERE claveMateria = %s AND carnetAlumno = %s
               ORDER BY numOportunidad ASC
               LIMIT 1
            """

    result = con.execute_query(query, (studentClave,subjectClave), True).fetchone()
    #primera oportunidad de alumno de reingreso
    if result == None:
        return 1

    return result[0] + 1

"""
    Agrega materia a alumno solo si pasa por algunas validacioens
"""
def addSubjectToSchedule(studentClave, groupClave, subjectClave):
    estatus = loadStudentStatus(studentClave)

    #if not validateInscriptionHour(studentClave):
    #    return "No es tu tiempo de inscripción"

    requiredSubject= isRequiredSubject(subjectClave, studentClave)
    if requiredSubject:
        return "Debes aprobar antes: {0}".format(requiredSubject)

    scheduleUsed = isScheduleUsed(groupClave,studentClave, subjectClave)
    #if scheduleUsed:
    #    return "Horario empalmado con {0}, selecciona otra opción".format(scheduleUsed[1])

    #Validar cantidad en grupo
    counter = checkCounterInGroup(groupClave,subjectClave)
    capacity = checkCapacityInGroup(groupClave,subjectClave)
    ##checar capacidad
    if counter < capacity:
        subjectOportunity = 1  #si es primer ingreso

        if estatus == 'REINGRESO':
            subjectOportunity = findSubjectOportunity(studentClave,subjectClave)

        query = """
                INSERT INTO Oportunidad (calificacion, numOportunidad, carnetAlumno,claveMateria)
                VALUES (%s, %s, %s, %s)
                """
        con.execute_query(query, (0,subjectOportunity,studentClave,subjectClave),False,True)

        query = """
                INSERT INTO Alumno_Grupo (claveGrupo, carnetAlumno)
                VALUES (%s, %s)
                """
        con.execute_query(query, (groupClave, studentClave),False,True)

        updateGroupCounter(counter, groupClave, subjectClave)

        return "Materia inscrita"

    return "Lo sentimos, grupo lleno, elige otra opción"
