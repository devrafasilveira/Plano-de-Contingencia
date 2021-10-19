from mysql.connector import Error

class RecoverDB:
    def __init__(self, connection):
        self.connection = connection

    def updateDate(self, recover):
        try:
            sql = 'UPDATE newuser SET password = %s, r_password = %s WHERE user = %s'
            cursor = self.connection.cursor()
            cursor.execute(sql, (recover.password, recover.r_password, recover.user))
            self.connection.commit()
            return True
        except Error as e:
            print('Error: ',e)
            return False