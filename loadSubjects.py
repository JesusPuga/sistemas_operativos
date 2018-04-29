import BDConexion
from BDConexion import *
import os

con = Conexion(os.environ['USER_SISTEMAS'],
               os.environ['PASSWORD_SISTEMAS'],
               "FacultadBD")

def loadAllSubjects():

    query = """SELECT nombre FROM Materia"""
    result = con.execute_query(query,(), True)

    return result

def loadSubjectGroups(subject):

    query = """SELECT Grupo.claveGrupo
               FROM  Grupo
               INNER JOIN Materia ON Materia.claveMateria = Grupo.claveMateria AND
                                     Materia.nombre = %s"""

    result = con.execute_query(query,(subject,), True)

    return result
