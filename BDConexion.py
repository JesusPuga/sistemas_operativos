import MySQLdb as MariaDB

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

    def execute_query(self, query_p, parametros =()):
        cursor = self.conn.cursor()
        result = cursor.execute(query_p, parametros)
