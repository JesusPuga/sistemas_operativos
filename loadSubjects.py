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
