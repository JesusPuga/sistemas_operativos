from SQL.BDConexion import *
import os

def loadAllSubjects():
    con = createConection()
    query = """SELECT nombre FROM Materia"""
    result = con.execute_query(query,(), True)
    del con
    return result

def loadSubjectGroups(subject):
    con = createConection()
    query = """SELECT Grupo.claveGrupo
               FROM  Grupo
               INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria AND
                                     Materia.nombre = %s"""

    result = con.execute_query(query,(subject,), True)
    del con
    return result

def loadAvailableSubjects(clave):
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

    con = createConection()
    #REVISAR ESTATUS DE ALUMNO
    query= """SELECT Alumno.estatus FROM Alumno WHERE Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(clave,),True)

    #CAPTURA DEL CONTENIDO DE LA CONSULTA. SE GUARDA EL ESTATUS DEL ALUMNO ("PRIMER INGRESO", "REINGRESO", "NO INSCRITO")"
    for x in result: estatus=x[0]

    #CASO ALUMNO INSCRITO Y DE REINGRESO
    if  estatus == 'REINGRESO':
        query="""
                 SELECT Materia.claveMateria, Materia.nombre,
                        Materia.semestre, Materia.creditos
                 FROM Materia
                 LEFT JOIN Oportunidad
                 ON Oportunidad.claveMateria = Materia.claveMateria AND
                    Oportunidad.carnetAlumno = %s
                 WHERE Oportunidad.claveMateria IS NULL OR
                       (Oportunidad.calificacion < 70 AND Oportunidad.calificacion != 0)
                 ORDER BY Materia.claveMateria DESC
              """
        result = con.execute_query(query,(clave,),True,True)

    if result == 0:
        print("HUBO UN ERROR")

    del con
    return result

def loadAvailableGroups(subject):
    con = createConection()

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

    del con
    return result

def loadRegisteredSubjects(studentClave):
    con = createConection()
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

    del con
    return result

def eraseSubject(studentClave, groupClave, subjectClave):
    con = createConection()
    args = (studentClave, groupClave, subjectClave)
    con.call_procedures('borradoGrupo', args)
    del con