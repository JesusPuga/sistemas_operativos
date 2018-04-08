import BDConexion
from BDConexion import *

con = Conexion("root","run maria run","FacultadBD")

def validateUser(type,user, password):

    if type != "Alumno" and type != "Administrativo" and type != "Docente":
        return "Tipo de usuario inexistente"

    query = """SELECT carnetUsuario, tipoUsuario
               FROM Usuario
               WHERE carnetUsuario = %s and tipoUsuario = %s"""
    result = con.execute_query(query, (user,type))

    if result == None:
        return "Usuario equivocado"

    query = """SELECT carnetUsuario, tipoUsuario, contrasenia
               FROM Usuario
               WHERE contrasenia = %s and tipoUsuario = %s and carnetUsuario= %s"""
    result = con.execute_query(query, (password, type, user))

    if result == None:
        return "Contraseña equivocada"

    return "ok"


print(validateUser("Alumnos","user","password"))