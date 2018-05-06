import BDConexion
from BDConexion import *
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
               INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.claveGrupo AND
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

def loadStudentCredits(studentClave, period = "2018-01-16"):
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
