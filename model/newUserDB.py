from mysql.connector import Error

class NewUserDB:
    def __init__(self, connection):
        self.connection = connection

    def insertDate(self, newuser):
        try:
            sql = 'INSERT INTO newuser (name, registry, user, password, r_password) VALUES (%s, %s, %s, %s, %s)'
            cursor = self.connection.cursor()
            cursor.execute(sql, (newuser.name, newuser.registry, newuser.user, newuser.password, newuser.r_password))
            self.connection.commit()
            return True
        except Error as e:
            print('Error: ',e)
            return False
    
    def checking_login(self):
        cursor.execute('SELECT user FROM newuser') 
        result = cursor.fetchall() 
        list_user = []
        for x in result:
            a = ''.join(x)
            list_user.append(a)
        cursor.execute('SELECT password FROM newuser')
        result = cursor.fetchall() 
        list_pass = []
        for x in result:
            a = ''.join(x)
            list_pass.append(a)
        return list_user + list_pass
        