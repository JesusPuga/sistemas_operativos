from SQL.BDConexion import *
import os
from tkinter import messagebox

# Retorna maestro y alumno desde Usuario, por lo tanto se repiten el resto de los datos
def loadSubjectsForStudent(carnetAlumno):
    con = createConection()
    query = """SELECT DISTINCT Materia.claveMateria, Materia.nombre, Usuario.nombre,
                               Usuario.apellidoPaterno, Usuario.apellidoMaterno
               FROM Materia
               INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria
               INNER JOIN Empleado ON Empleado.carnetEmpleado = Grupo.carnetEmpleado
               INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo AND
                                          Alumno_Grupo.carnetAlumno = %s
               INNER JOIN Usuario ON  Empleado.carnetEmpleado = Usuario.carnetUsuario
               ORDER BY Grupo.claveMateria DESC"""

    result = con.execute_query(query,(carnetAlumno,), True)
    del con
    return result

def loadStudentsForGroup(group,subject):
    con = createConection()
    query = """SELECT DISTINCT Alumno_Grupo.carnetAlumno,Usuario.nombre, Usuario.apellidoPaterno,Usuario.apellidoMaterno
               FROM Materia_Seriada
               INNER JOIN Materia ON Materia.ClaveMateria = Materia_Seriada.ClaveMateria AND
                                     Materia.nombre = %s
               INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND
                                   Grupo.claveGrupo = %s
               INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.claveGrupo
               INNER JOIN Usuario ON Alumno_Grupo.carnetAlumno = Usuario.carnetUsuario
               ORDER BY Alumno_Grupo.carnetAlumno DESC"""

    result = con.execute_query(query,(subject,group), True)
    del con
    return result

def loadStudentStatus(clave):
    con = createConection()
    #REVISAR ESTATUS DE ALUMNO
    query= """SELECT Alumno.estatus FROM Alumno WHERE Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(clave,),True)

    #CAPTURA DEL CONTENIDO DE LA CONSULTA. SE GUARDA EL ESTATUS DEL ALUMNO ("PRIMER INGRESO", "REINGRESO", "NO INSCRITO")"
    for x in result:
        estatus=x[0]

    del con
    return estatus

def loadStudentCredits(studentClave, period = "180116"):
    con = createConection()
    query = """
                SELECT COUNT(*)
                FROM Alumno_Grupo
                INNER JOIN Grupo
                ON Grupo.IDGrupo  = Alumno_Grupo.claveGrupo AND
                   periodo = %s AND
                   Alumno_Grupo.carnetAlumno = %s;
            """

    result = con.execute_query(query,(period,studentClave), True)
    del con
    return result.fetchone()[0]

def loadStudentSchedule(studentClave):
    con = createConection()
    query="""
            SELECT  CONCAT(H.horaInicio,' - ',H.horaFin) Hora,
                    MAX(CASE WHEN H.dia = 'Lunes' THEN H.nombre ELSE '' END) Lunes,
                    MAX(CASE WHEN H.dia = 'Martes' THEN H.nombre ELSE '' END) Martes,
                    MAX(CASE WHEN H.dia = 'Miercoles' THEN H.nombre ELSE '' END) Miercoles,
                    MAX(CASE WHEN H.dia = 'Jueves' THEN H.nombre ELSE '' END) Jueves,
                    MAX(CASE WHEN H.dia = 'Viernes' THEN H.nombre ELSE '' END) Viernes,
                    MAX(CASE WHEN H.dia = 'Sabado' THEN H.nombre ELSE '' END) Sabado
            FROM (SELECT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Docente, Dia.dia, Horario.horaInicio, Horario.horaFin
                    FROM Materia
                    INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
                    INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
                    INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
                    INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
                    INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
                    INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
                    INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
                    WHERE Alumno.carnetAlumno = %s) AS H
            GROUP BY CONCAT(Horario.horaInicio,' - ',Horario.horaFin)
            ORDER BY CONCAT(Horario.horaInicio,' - ',Horario.horaFin) DESC
          """

    result = con.execute_query(query,(studentClave,),True)
    del con
    return result

def loadAllStudentSubjects(studentClave):
    con = createConection()
    query="""
            SELECT DISTINCT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Nombre
            FROM Materia
            INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
            INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
            INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
            INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
            INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
            INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
            INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
            WHERE Alumno.carnetAlumno = %s
            ORDER BY Materia.claveMateria DESC
          """

    result = con.execute_query(query,(studentClave,),True)
    del con
    return result
