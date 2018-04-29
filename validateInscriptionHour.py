import BDConexion
from BDConexion import *
from datetime import *


con = Conexion(os.environ['USER_SISTEMAS'],
               os.environ['PASSWORD_SISTEMAS'],
               "FacultadBD")

##Retorna True si es posible continuar inscribiendo
##        False en caso contrario
def validateInscriptionHour(carnetAlumno):
    query = """SELECT Inscripcion.fechaInscripcion
               FROM Inscripcion
               INNER JOIN Alumno
                     ON Alumno.claveInscripcion = Inscripcion.claveInscripcion AND
                        Alumno.carnetAlumno = %s"""
    result = con.execute_query(query,(carnetAlumno,), True)

    for inscriptionDate in result:
        if inscriptionDate[0] + timedelta(hours = 2) > datetime.now() or inscriptionDate[0]  < datetime.now() :
            print(inscriptionDate[0])
            return False

    return True
