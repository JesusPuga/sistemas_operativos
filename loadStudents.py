import BDConexion
from BDConexion import *
import os

con = Conexion(os.environ['USER_SISTEMAS'],
               os.environ['PASSWORD_SISTEMAS'],
               "FacultadBD")
#¿por grupo o por materia?
def loadStudentsForStudent():

    query = """SELECT Grupo.periodo,Alumno_Grupo.carnetAlumno, Grupo.claveMateria,Dia.dia, Horario.horaFin, Horario.horaInicio
               FROM  Alumno_Grupo
               INNER JOIN Grupo ON Grupo.IDGrupo = Alumno_Grupo.claveGrupo and Alumno_Grupo.carnetAlumno = 1
               INNER JOIN Horario ON Horario.claveGrupo  = Grupo.claveGrupo
               INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
               INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
               ORDER BY Alumno_Grupo.carnetAlumno"""
    result = con.execute_query(query,(carnetAlumno,), True)

    return result

##Agregar selección de grupo
def loadStudentsForGroup(group,subject):

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

    return result
