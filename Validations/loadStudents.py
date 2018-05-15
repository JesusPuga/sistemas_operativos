from SQL.BDConexion import *
import os
from tkinter import messagebox
from datetime import *

# Retorna maestro y alumno desde Usuario, por lo tanto se repiten el resto de los datos
def loadSubjectsForStudent(carnetAlumno, period = "180116"):
    con = createConection()
    query = """SELECT DISTINCT Materia.claveMateria, Materia.nombre, Usuario.nombre,
                               Usuario.apellidoPaterno, Usuario.apellidoMaterno
               FROM Materia
               INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND
                                   Grupo.periodo = %s
               INNER JOIN Empleado ON Empleado.carnetEmpleado = Grupo.carnetEmpleado
               INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo AND
                                          Alumno_Grupo.carnetAlumno = %s
               INNER JOIN Usuario ON  Empleado.carnetEmpleado = Usuario.carnetUsuario
               ORDER BY Grupo.claveMateria DESC"""

    result = con.execute_query(query,(period,carnetAlumno), True)
    del con
    return result

def loadStudentsForGroup(group,subject, period = "180116"):
    con = createConection()
    query = """SELECT DISTINCT Alumno_Grupo.carnetAlumno,Usuario.nombre, Usuario.apellidoPaterno,Usuario.apellidoMaterno
               FROM Materia_Seriada
               INNER JOIN Materia ON Materia.ClaveMateria = Materia_Seriada.ClaveMateria AND
                                     Materia.nombre = %s
               INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND
                                   Grupo.claveGrupo = %s AND
                                   Grupo.periodo = %s
               INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.claveGrupo
               INNER JOIN Usuario ON Alumno_Grupo.carnetAlumno = Usuario.carnetUsuario
               ORDER BY Alumno_Grupo.carnetAlumno DESC"""

    result = con.execute_query(query,(subject,group, period), True)
    del con
    return result

def loadStudentStatus(clave):
    con = createConection()
    #REVISAR ESTATUS DE ALUMNO
    query= """SELECT Alumno.estatus FROM Alumno WHERE Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(clave,),True)

    #CAPTURA DEL CONTENIDO DE LA CONSULTA. SE GUARDA EL ESTATUS DEL ALUMNO ("PRIMER INGRESO", "REINGRESO", "NO INSCRITO")"
    for x in result:
        estatus=x[0]

    del con
    return estatus

def loadStudentCredits(studentClave, period = "180116"):
    con = createConection()
    query = """
                SELECT COUNT(*)
                FROM Alumno_Grupo
                INNER JOIN Grupo
                ON Grupo.IDGrupo  = Alumno_Grupo.claveGrupo AND
                   periodo = %s AND
                   Alumno_Grupo.carnetAlumno = %s;
            """

    result = con.execute_query(query,(period,studentClave), True)
    del con
    return result.fetchone()[0]

def loadStudentSchedule(studentClave):
    con = createConection()
    query="""
            SELECT  CONCAT(H.horaInicio,' - ',H.horaFin) Hora,
                    MAX(CASE WHEN H.dia = 'Lunes' THEN H.nombre ELSE '' END) Lunes,
                    MAX(CASE WHEN H.dia = 'Martes' THEN H.nombre ELSE '' END) Martes,
                    MAX(CASE WHEN H.dia = 'Miercoles' THEN H.nombre ELSE '' END) Miercoles,
                    MAX(CASE WHEN H.dia = 'Jueves' THEN H.nombre ELSE '' END) Jueves,
                    MAX(CASE WHEN H.dia = 'Viernes' THEN H.nombre ELSE '' END) Viernes,
                    MAX(CASE WHEN H.dia = 'Sabado' THEN H.nombre ELSE '' END) Sabado
            FROM (SELECT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Docente, Dia.dia, Horario.horaInicio, Horario.horaFin
                    FROM Materia
                    INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
                    INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
                    INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
                    INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
                    INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
                    INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
                    INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
                    WHERE Alumno.carnetAlumno = %s) AS H
            GROUP BY CONCAT(Horario.horaInicio,' - ',Horario.horaFin)
            ORDER BY CONCAT(Horario.horaInicio,' - ',Horario.horaFin) DESC
          """

    result = con.execute_query(query,(studentClave,),True)
    del con
    return result

def loadAllStudentSubjects(studentClave):
    con = createConection()
    query="""
            SELECT DISTINCT Materia.claveMateria, Grupo.claveGrupo, Materia.nombre,CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Nombre
            FROM Materia
            INNER JOIN Grupo ON Grupo.claveMateria = Materia.claveMateria AND Grupo.periodo = "180116"
            INNER JOIN Alumno_Grupo ON Alumno_Grupo.claveGrupo = Grupo.IDGrupo
            INNER JOIN Alumno ON Alumno.carnetAlumno = Alumno_Grupo.carnetAlumno
            INNER JOIN Usuario ON Usuario.carnetUsuario = Grupo.carnetEmpleado
            INNER JOIN Horario ON Horario.claveGrupo = Alumno_Grupo.claveGrupo
            INNER JOIN Dia_Horario ON Dia_Horario.IDHorario = Horario.IDHorario
            INNER JOIN Dia ON Dia.IDDia = Dia_Horario.IDDia
            WHERE Alumno.carnetAlumno = %s
            ORDER BY Materia.claveMateria DESC
          """

    result = con.execute_query(query,(studentClave,),True)
    del con
    return result

def loadSutdentInf(studentClave):
    con = createConection()
    query="""
            SELECT Alumno.carnetAlumno, CONCAT(Usuario.nombre,' ',Usuario.apellidoPaterno) AS Nombre, Carrera.nombre
            FROM Alumno
            INNER JOIN Usuario ON Usuario.carnetUsuario = Alumno.carnetAlumno
            INNER JOIN Carrera ON Carrera.claveCarrera = Alumno.claveCarrera
            WHERE Alumno.carnetAlumno = %s
          """

    result = con.execute_query(query,(studentClave,),True)
    del con
    return result

def loadAllCareers():
    con = createConection()
    query="""
            SELECT nombre
            FROM Carrera
          """

    result = con.execute_query(query,(),True)

    del con
    return result

def loadAvailableDatesInscription():
    con = createConection()
    query="""
            SELECT fechaInscripcion
            FROM Inscripcion
            WHERE fechaInscripcion = %s
          """
    now = str(datetime.now()).split(".")[0] #quir decimals in date
    result = con.execute_query(query,(now,),True)
    del con
    return result

def insertStudent(clave,status, inscriptionClave,sex,cel, password, name, lastName, lastName2):
    con = createConection()
    query = """
            INSERT INTO Alumno (estatus, claveCarrera, claveInscripcion)
            VALUES (%s, 1, 1)
            """
    con.execute_query(query, (status, inscriptionClave),False,True)
    ##traer la clave del registro agregado para crear la inf

    query = """
            INSERT INTO Usuario (sexo, telefono, contrasenia, nombre, apellidoPaterno, apellidoMaterno, tipoUsuario)
            VALUES ( %s, %s, %s,%s, %s, %s, 1)
            """
    con.execute_query(query, (sex,cel, password, name, lastName, lastName2),False,True)

    if status = "REINGRESO":
        ## deben ponerse todas las materias anteriores como pasadas
    else:
        #debe tenner creado un horario xD

    del con
    return result

def insertInscription(fechaInscripcion = True):
    con = createConection()
    query = """
            INSERT INTO Inscription (fechaInscripcion)
            VALUES (%s)
            """
    now = str(datetime.now()).split(".")[0] #quir decimals in date
    con.execute_query(query, (now,),False,True)
    del con
