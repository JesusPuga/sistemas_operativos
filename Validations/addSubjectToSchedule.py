import os
from SQL.BDConexion import *
from Validations.loadStudents import *
from datetime import *

"""Retorna True si es posible continuar inscribiendo
       False en caso contrario
"""
def validateInscriptionHour(carnetAlumno):
    con = createConection()
    query = """SELECT Inscripcion.fechaInscripcion
               FROM Inscripcion
               INNER JOIN Alumno
                     ON Alumno.claveInscripcion = Inscripcion.claveInscripcion AND
                        Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(carnetAlumno,), True)

    for inscriptionDate in result:
        if  datetime.now() > inscriptionDate[0] + timedelta(hours = 2) or datetime.now() < inscriptionDate[0]:
            print(datetime.now() > inscriptionDate[0] + timedelta(hours = 2))
            print(datetime.now() < inscriptionDate[0])
            return (False,inscriptionDate[0])

    del con
    return (True,inscriptionDate[0])

"""
    Verifica si la materia depende de aprobar algún otra
        -Retorna False en caso de no requrir aprobar alguna materia
        -Retorna un String con el nombre de la materia que necesita pasar
            +String se toma como True en una validación
"""
def isRequiredSubject(subjectClave, studentClave):
    con = createConection()
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

            del con
            return subjectInf[0] #python toma una String comoo True

    del con
    return False

"""
    Verifica si el horario del grupo se empalma con algún otro
        -Retorna Materia empalmada en caso de que se empalme
        -Retorna False en caso contrario
"""
def isScheduleUsed(groupId,studentClave, period= "180116"):
    con = createConection()
    query = """
            SELECT Materia.nombre,Dia_Horario.IDDia,Horario.horaInicio, Horario.HoraFin
            FROM Grupo
            INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria AND
                                  Grupo.IDGrupo = %s AND
                                  Grupo.periodo = %s
            INNER JOIN Horario ON Horario.claveGrupo = Grupo.IDGrupo
            INNER JOIN Dia_Horario  ON Dia_Horario.IDHorario = Horario.IDHorario;

            """
    result = con.execute_query(query, (groupId,period), True)

    for nombre, claveDia, startHour, finishHour in result:
        query = """
                    SELECT Dia_Horario.IDDia, Materia.nombre,Horario.horaInicio, Horario.HoraFin
                    FROM Alumno_Grupo
                    INNER JOIN Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo  AND
                                        Alumno_Grupo.carnetAlumno = %s AND
                                        Grupo.periodo = %s
                    INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria
                    INNER JOIN Horario ON Horario.claveGrupo = Grupo.IDGrupo AND
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
            del con
            return  schedulesFound

    del con
    return False

"""
    Retorna cantidad de alumnos inscritos en una materia
"""
def checkCounterInGroup(groupClave, subjectClave, periodo = "180116"):
    con = createConection()
    query = """SELECT contador
               FROM Grupo
               WHERE claveGrupo = %s AND claveMateria = %s AND periodo = %s
            """
    result = con.execute_query(query, (groupClave, subjectClave,periodo), True)

    del con
    return result.fetchone()[0]
"""
    Retorna la capacidad del grupo dependiendo la materia y el periodo
"""
def checkCapacityInGroup(groupClave, subjectClave, periodo = "180116"):
    con = createConection()
    query = """
                SELECT capacidad
                FROM Grupo
                WHERE claveGrupo = %s AND claveMateria = %s AND periodo = %s
            """
    result = con.execute_query(query, (groupClave, subjectClave,periodo), True)

    del con
    return result.fetchone()[0]
"""
    Actualiza contador en grupo
"""
def updateGroupCounter(counter,groupClave, subjectClave, periodo = "180116"):
    con = createConection()
    query = """UPDATE Grupo SET contador = %s
               WHERE claveGrupo = %s AND claveMateria = %s AND periodo = %s;
            """

    con.execute_query(query, (counter + 1,groupClave, subjectClave,periodo), False, True)
    del con

"""
    Retorna la oportunidad actual de una materia dependiendo el alumno
"""
def findSubjectOportunity(studentClave,subjectClave):
    con = createConection()
    query = """SELECT numOportunidad
               FROM Oportunidad
               WHERE claveMateria = %s AND carnetAlumno = %s
               ORDER BY numOportunidad ASC
               LIMIT 1
            """

    result = con.execute_query(query, (studentClave,subjectClave), True).fetchone()
    #primera oportunidad de alumno de reingreso
    if result == None:
        del con
        return 1

    del con
    return result[0] + 1

"""
    Agrega materia a alumno solo si pasa por algunas validacioens
"""
def addSubjectToSchedule(studentClave, groupId, groupClave, subjectClave):
    estatus = loadStudentStatus(studentClave)

    inscriptionHour = validateInscriptionHour(studentClave)[0]
    if not inscriptionHour[0]:
        return "Tiempo terminado, hora: {0}".format(inscriptionHour[1].split(" ")[1])

    requiredSubject= isRequiredSubject(subjectClave, studentClave)
    if requiredSubject:
        return "Debes aprobar antes: {0}".format(requiredSubject)

    scheduleUsed = isScheduleUsed(groupId,studentClave)
    if scheduleUsed:
        return "Horario empalmado con {0}, selecciona otra opción".format(scheduleUsed[1])

    #Validar cantidad en grupo
    counter = checkCounterInGroup(groupClave,subjectClave)
    capacity = checkCapacityInGroup(groupClave,subjectClave)

    if counter < capacity:
        subjectOportunity = 1  #si es primer ingreso

        if estatus == 'REINGRESO':
            subjectOportunity = findSubjectOportunity(studentClave,subjectClave)

        con = createConection()
        query = """
                INSERT INTO Oportunidad (calificacion, numOportunidad, carnetAlumno,claveMateria)
                VALUES (%s, %s, %s, %s)
                """
        con.execute_query(query, (0,subjectOportunity,studentClave,subjectClave),False,True)

        query = """
                INSERT INTO Alumno_Grupo (claveGrupo, carnetAlumno)
                VALUES (%s, %s)
                """
        con.execute_query(query, (groupId, studentClave),False,True)

        del con

        updateGroupCounter(counter, groupClave, subjectClave)

        return "Materia inscrita"

    return "Lo sentimos, grupo lleno, elige otra opción"
