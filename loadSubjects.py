import BDConexion
from BDConexion import *
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
