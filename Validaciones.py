import BDConexion
from BDConexion import *

con = Conexion("root","run maria run","FacultadBD")

def student_inf():
    query_p= "SELECT * FROM Alumno"
    con.execute_query(query_p)


student_inf()
