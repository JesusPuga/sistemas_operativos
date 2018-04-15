import BDConexion
from BDConexion import *

con = Conexion("root","run maria run","FacultadBD")

def validateUser(type, user, password):
    typeUser = {"Alumno":"1","Docente":"2","Adminstrativo":"3"}

    if type != "Alumno" and type != "Docente" and type != "Administrativo":
        return "Tipo de usuario inexistente"

    query = """SELECT carnetUsuario, tipoUsuario
               FROM Usuario
               WHERE carnetUsuario = %s and tipoUsuario = %s"""
    result = con.execute_query(query,(user, typeUser[type]))

    if result == 0:
        return "Usuario equivocado"

    query = """SELECT carnetUsuario, tipoUsuario, contrasenia
               FROM Usuario
               WHERE contrasenia = %s  and carnetUsuario= %s and tipoUsuario = %s"""
    result = con.execute_query(query, (password,user,typeUser[type]))

    if result == 0:
        return "Contraseña equivocada"

    return "ok"

def findAvailableSubjects(clave):
    ##no se toma en cuenta el periodo del Usuario_Horario
    query = """SELECT Materia.ClaveMateria, Materia.nombre,
                      Materia.numeroSemestre, Materia.creditos
               FROM  Usuario_Horario
               INNER JOIN Horario ON Usuario_Horario.carnetAlumno = %s and
                                     Horario.claveHorario = Usuario_Horario.claveHorario
               INNER JOIN Oportunidad ON Oportunidad.IDOportunidad = Horario.claveOportunidad  and
                                         Oportunidad.calificacion >69
               INNER JOIN Materia ON Materia.ClaveMateria != Horario.ClaveMateria
               ORDER BY Materia.ClaveMateria desc;
            """
    result = con.execute_query(query, (clave,),True)
    ##¿NO HAY MATERIAS POR CURSAR? V:, YA VALIÓ
    if result == 0:
        return "Parece que ha habido algún problema, shales, wait a moment"

    return result

def findAvailableTeachers(subject, availableGroup = True):
    #Datos aleatorios
    values = []
    print(subject)
    if "FUNDAMENTOS DE ELECTROMAGNETISMO" in subject and availableGroup:
        values.extend([(1,2,3,
                        {"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),
                       (5,6,7,
                        {"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "FUNDAMENTOS DE ALGORITMOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "ARQUITECTURA DE COMPUTADORAS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "PROGRAMACIÓN ESTRUCTURADA" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "MATEMÁTICAS I" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "MATEMÁTICAS II" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "SISTEMAS ELECTRÓNICOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "FUNDAMENTOS DE REDES" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "PROGRAMACIÓN ORIENTADA A OBJETOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "FUNDAMENTOS DE ESTADÁSTICA" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "MATEMÁTICAS DISCRETAS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "CIRCUITOS DIGITALES" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "ESTRUCTURA DE DATOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "ANÁLISIS DE SISTEMAS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "TEORÍA DE AUTÁMATAS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "ANÁLISIS NUMÉRICO" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "ADMINISTRACIÓN DE PROYECTOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "SISTEMAS OPERATIVOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "ADMINISTRACIÓN DE REDES" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "MODELOS ESTADÍSTICOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "SISTEMAS EMBEBIDOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "MINERÍA DE Datos" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "SISTEMA DISTRIBUIDOS" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "INTELIGENCIA ARTIFICIAL" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])
    elif "BIG DATA" in subject and availableGroup:
        values.extend([(1,2,3,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]}),(5,6,7,{"Lunes":["1:30","2:30"],"Martes":["1:30","2:30"]})])

    return values

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
                           `claveMateria`,`claveOportunidad`,`claveGrupo`)
               VALUES ("day", '15:30:00', '16:30:00', %s, %s, %s);
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
