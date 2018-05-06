import BDConexion
from BDConexion import *
import os

con = Conexion(os.environ['USER_SISTEMAS'],
               os.environ['PASSWORD_SISTEMAS'],
               "FacultadBD")

def validateUser(type, user, password):
    typeUser = {"Alumno":"1","Docente":"2","Administrativo":"3"}

    if type != "Alumno" and type != "Docente" and type != "Administrativo":
        return "TIPO DE USUARIO INEXISTENTE"

    query = """SELECT carnetUsuario, tipoUsuario
               FROM Usuario
               WHERE carnetUsuario = %s and tipoUsuario = %s"""
    result = con.execute_query(query,(user, typeUser[type]))

    if result == 0:
        return "USUARIO INCORRECTO"

    query = """SELECT carnetUsuario, tipoUsuario, contrasenia
               FROM Usuario
               WHERE contrasenia = %s  and carnetUsuario= %s and tipoUsuario = %s"""
    result = con.execute_query(query, (password,user,typeUser[type]))

    if result == 0:
        return "CONTRASEÑA INCORRECTA"

    return "ok"

def findAvailableSubjects(clave):
    """ Función que busca las materias disponibles a cursar del alumno

    El primer paso es verificar el ESTATUS del alumno. Esto ayudará a determinar si el
    alumno
        a) Está inscrito al periodo vigente
            -Si es de primer ingreso
            -Si es de reingreso
        b) No está inscrito al periodo vigente

    Si el alumno es de primer ingreso, no registra materias. Previamente hubo algún proceso
    administrativo en el cual se le asignó un horario definido.

    Si el alumno es de reingreso, se hará un despliegue de:
        -Materias reprobadas, en su n-ésima oportunidad
        -Materias de semestres siguientes

    Si el alumno no está inscrito, el sistema simplemente da aviso de ello e invalida la opción
    de inscripción.
    """

    #REVISAR ESTATUS DE ALUMNO
    query= """SELECT Alumno.estatus FROM Alumno WHERE Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(clave,),True)

    #CAPTURA DEL CONTENIDO DE LA CONSULTA. SE GUARDA EL ESTATUS DEL ALUMNO ("PRIMER INGRESO", "REINGRESO", "NO INSCRITO")"
    for x in result: estatus=x[0]

    #CASO ALUMNO INSCRITO Y DE REINGRESO
    if  estatus == 'REINGRESO':
        query="""SELECT Materia.claveMateria, Materia.nombre,
                        Materia.semestre, Materia.creditos
                FROM Materia
                INNER JOIN Oportunidad
                ON Oportunidad.claveMateria != Materia.claveMateria AND Oportunidad.calificacion > 70 AND Oportunidad.carnetAlumno = %s
                ORDER BY ClaveMateria DESC
        """
        result = con.execute_query(query,(clave,),True)

    if result == 0:
        print("HUBO UN ERROR")

    return result

def findAvailableGroups(subject):
    query="""SELECT Grupo.claveGrupo, Grupo.aula, CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Nombre,
            Dia.dia, MIN(Horario.horaInicio), MAX(Horario.horaFin), Grupo.claveMateria, Grupo.IDGrupo
            FROM Grupo
            INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria
            INNER JOIN Horario ON Horario.claveGrupo = Grupo.IDGrupo
            INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
            INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
            INNER JOIN Empleado ON Empleado.carnetEmpleado = Grupo.carnetEmpleado
            INNER JOIN Usuario ON Usuario.carnetUsuario = Empleado.carnetEmpleado
            WHERE Materia.claveMateria = %s
            GROUP BY Grupo.claveGrupo, Dia.dia
            ORDER BY Grupo.claveGrupo  DESC
    """
    result = con.execute_query(query,(subject,),True)

    if result == 0:
        print("HUBO UN ERROR")

    return result

def findStudentSchedule(studentClave):
    query="""SELECT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Nombre, Dia.dia, Horario.horaInicio, Horario.horaFin
    FROM Materia
    INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
    INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
    INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
    INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
    INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
    INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
    INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
    WHERE Alumno.carnetAlumno = %s"""

    result = con.execute_query(query,(studentClave,),True)

    return result


def findSubjectOportunity(studentClave, subjectClave):
    #Número de veces que se ha registrado la materia
    query = """SELECT COUNT(*) FROM Usuario_Horario
               JOIN Horario ON Usuario_Horario.claveHorario = Horario.claveHorario
                            and Usuario_Horario.carnetAlumno = %s
                            and Horario.claveMateria = %s;
            """

    result = con.execute_query(query, (studentClave,subjectClave), True)

    return result.fetchone()[0] + 1

def isScheduleUsed(startHour,finishHour,studentClave, period):
    #se toman solo los horarios del periodo actual tomando en cuenta el periodo
    query = """SELECT COUNT(*)
               FROM Usuario_Horario
               JOIN Horario ON Usuario_Horario.carnetAlumno  = %s and
                               Usuario_Horario.claveHorario  = Horario.claveHorario and
                               Usuario_Horario.periodo = %s and
                               (
                                (Horario.horaInicio >= %s and
                                 Horario.horaInicio < %s) or
                                (Horario.horaFin > %s and
                                 Horario.horaFin <= %s)
                               )

            """
    print(query)
    result = con.execute_query(query,
                               (studentClave,period,startHour,finishHour,startHour,finishHour),
                               True)

    return True if result.fetchone()[0] > 0 else False

def checkCounterInGroup(groupClave, classroomClave, teacherClave):
    query = """SELECT contador
               FROM Grupo
               WHERE claveGrupo = %s and aula = %s and claveEmpleado = %s;
            """
    result = con.execute_query(query, (groupClave, classroomClave,teacherClave), True)

    return result.fetchone()[0]

def updateGroupCounter(counter,groupClave, classroomClave, teacherClave):
    query = """UPDATE Grupo SET contador = %s
               WHERE claveGrupo = %s and aula = %s and claveEmpleado = %s;
            """

    con.execute_query(query, (counter + 1,groupClave,classroomClave,teacherClave), False, True)

def addSubjectToSchedule(studentClave, subjectClave, groupClave):
    subjectOportunity = findSubjectOportunity(studentClave, subjectClave)
    startHour = "15:30:00"
    finishHour = "16:00:00"
    period = "Administrativo"

    query = """INSERT INTO `Horario` (`dia`,`horaInicio`,`horaFin`,
                           `claveMateria`, `claveGrupo`)
               VALUES ("day", '15:30:00', '16:30:00', %s, %s);
            """
    #Validar empalme de horario
    if isScheduleUsed(startHour, finishHour, studentClave, period):
        return "Horario empalmado, selecciona otra opción"

    #Validar cantidad en grupo
    counter = checkCounterInGroup(groupClave,1,1)

    if counter < 30:
        con.execute_query(query, (subjectClave,subjectOportunity,groupClave),False,True)
        updateGroupCounter(counter,subjectClave,subjectOportunity,groupClave)
        return "Materia inscrita"

    return "Lo sentimos, grupo lleno, elige otra opción"

def simpleShowRegisteredSubject(studentClave):
    """Función que busca las metrias inscritas de un alumno"""

    query="""SELECT Materia.claveMateria, Materia.nombre, Grupo.IDGrupo
        FROM Materia
        INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria
        INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
        INNER JOIN Alumno ON Alumno_Grupo.carnetAlumno = Alumno.carnetAlumno
        WHERE Alumno.carnetAlumno = %s
        ORDER BY  claveMateria DESC
    """
    result = con.execute_query(query,(studentClave,),True)

    if result == 0:
        print("HUBO UN ERROR")

    return result

def eraseSubject(studentClave, groupClave, subjectClave):
    args = (studentClave, groupClave, subjectClave)
    con.call_procedures('borradoGrupo', args)
