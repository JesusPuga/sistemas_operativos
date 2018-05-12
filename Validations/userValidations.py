from SQL.BDConexion import *
import os

def validateUser(type, user, password):
    con = createConection()
    typeUser = {"Alumno":"1","Docente":"2","Administrativo":"3"}

    if type != "Alumno" and type != "Docente" and type != "Administrativo":
        return "TIPO DE USUARIO INEXISTENTE"

    query = """SELECT carnetUsuario, tipoUsuario
               FROM Usuario
               WHERE carnetUsuario = %s and tipoUsuario = %s"""
    result = con.execute_query(query,(user, typeUser[type]))

    if result == 0:
        return "USUARIO INCORRECTO"

    query = """SELECT carnetUsuario, tipoUsuario, contrasenia
               FROM Usuario
               WHERE contrasenia = %s  and carnetUsuario= %s and tipoUsuario = %s"""
    result = con.execute_query(query, (password,user,typeUser[type]))

    if result == 0:
        return "CONTRASEÑA INCORRECTA"

    del con
    return "ok"
