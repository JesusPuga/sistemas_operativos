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

def findAvailableSubjects(clave):
    ##no se toma en cuenta el periodo del Usuario_Horario
    query = """SELECT Materia.ClaveMateria, Materia.nombre,
                      Materia.numeroSemestre, Materia.creditos
               FROM  Usuario_Horario
               INNER JOIN Horario ON Usuario_Horario.carnetAlumno = %s and
                                     Horario.claveHorario = Usuario_Horario.claveHorario
               INNER JOIN Oportunidad ON Oportunidad.IDOportunidad = Horario.claveOportunidad  and
                                         Oportunidad.calificacion >69
               INNER JOIN Materia ON Materia.ClaveMateria != Horario.ClaveMateria
               ORDER BY Materia.ClaveMateria desc;
            """
    result = con.execute_query(query, (clave,),True)

    if result == 0:
        return "Parece que ha habido algún problema, shales, wait a moment"

    return result

def findAvailableTeachers(subject):
    #Datos aleatorios
    values = []
    print(subject)
    if "ELECTROMAGNETISMO" in subject:
        values.extend([(1,2,3,4),(5,6,7,8)])
    elif "ALGORITMOS" in subject:
        values.extend([(1,2,3,4),(1,2,3,4)])

    return values
