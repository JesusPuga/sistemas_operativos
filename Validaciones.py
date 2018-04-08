import BDConexion
from BDConexion import *

con = Conexion("root","run maria run","FacultadBD")

def validateUser(type, user, password):

    if type != "Alumno" and type != "Docente" and type != "Administrativo":
        return "Tipo de usuario inexistente"

    query = """SELECT carnetUsuario
               FROM Usuario
               WHERE carnetUsuario = %s"""
    result = con.execute_query(query,(user,))

    if result == 0:
        return "Usuario equivocado"

    query = """SELECT carnetUsuario, tipoUsuario, contrasenia
               FROM Usuario
               WHERE contrasenia = %s  and carnetUsuario= %s"""
    result = con.execute_query(query, (password,user))

    if result == 0:
        return "Contraseña equivocada"

    return "ok"
