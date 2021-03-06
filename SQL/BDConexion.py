import MySQLdb as MariaDB
import os

class Conexion:
    def __init__(self, user_p, password, bd_p):
        self.conn = None
        self.new_connection(user_p,password,bd_p)

    def __del__(self):
        if self.conn != None:
            self.conn.close

    def new_connection(self, user_p, password, bd_p):
        try:
            self.conn = MariaDB.connect(user=user_p,
                passwd=password,
                db=bd_p)
        except MariaDB.Error as e:
            print(e)

    def execute_query(self, query_p, parametros=(), returnCursor = False, commit= False):
        cursor = self.conn.cursor()
        result = cursor.execute(query_p, parametros)

        #updates, deletes, insert
        if commit:
            self.conn.commit()
        #Nos permite recuperar la inf
        if returnCursor:
            return cursor

        return result

    def call_procedures(self, nameProcedure, args=()):
        cursor = self.conn.cursor()

        result_args = cursor.callproc(nameProcedure, args)

        self.conn.commit()

        return result_args

def createConection():
    con = Conexion(os.environ['USER_SISTEMAS'],
                   os.environ['PASSWORD_SISTEMAS'],
                   "FacultadBD")
    return con
