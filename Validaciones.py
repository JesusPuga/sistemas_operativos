import BDConexion
from BDConexion import *

con = Conexion("root","run maria run","FacultadBD")

def validateUser(type, user, password):
    typeUser = {"Alumno":"1","Docente":"2","Adminstrativo":"3"}

    if type != "Alumno" and type != "Docente" and type != "Administrativo":
        return "Tipo de usuario inexistente"

    query = """SELECT carnetUsuario, tipoUsuario
               FROM Usuario
               WHERE carnetUsuario = %s and tipoUsuario = %s"""
    result = con.execute_query(query,(user, typeUser[type]))

    if result == 0:
        return "Usuario equivocado"

    query = """SELECT carnetUsuario, tipoUsuario, contrasenia
               FROM Usuario
               WHERE contrasenia = %s  and carnetUsuario= %s and tipoUsuario = %s"""
    result = con.execute_query(query, (password,user,typeUser[type]))

    if result == 0:
        return "Contraseña equivocada"

    return "ok"
