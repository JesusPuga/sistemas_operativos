import MySQLdb as MariaDB

class Conexion:
    def conectar(self):
        try:
            conexion = MariaDB.connect(user='root',
                passwd='FCFM',
                db='FacultadBD')
        except MariaDB.Error as e:
            print(e)
        else:
            conexion.close()

    def query(self, query, parametros =()):
        conn = conectar()
        cursor = conn.cursor()
        query_result = cursor.excute(query, parametros)
        return
