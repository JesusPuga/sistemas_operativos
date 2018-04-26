import BDConexion
from BDConexion import *

con = Conexion("root","FCFM","FacultadBD")

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

    query="""SELECT Materia.claveMateria, Materia.nombre
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
