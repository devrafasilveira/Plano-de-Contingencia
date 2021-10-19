from mysql.connector import Error

class EntranceDB:
    def __init__(self, connection):
        self.connection = connection

    def consultDate(self, entrance):
        try:
            sql = 'SELECT user, password FROM newuser'
            cursor = self.connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall() 
            list = []
            for x in result:
                a = ''.join(x)
            list.append(a)
            if entrance.user and entrance.password in list:
                return True
        except Error as e:
            print('Error: ',e)
            return False