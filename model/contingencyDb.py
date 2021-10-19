from model.contingency import Contingency
from mysql.connector import Error

class ContingencyDb:
    def __init__(self, connection):
        self.connection = connection

    def insertDate(self, contingency):
        try:
            sql = 'INSERT INTO contingency (pharmacy, room, professional, registry, datetime, bc1, bc2, bc3, bc4, qtr1, qtr2, qtr3, qtr4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            cursor = self.connection.cursor()
            cursor.execute(sql, (contingency.pharmacy, contingency.room, contingency.professional, contingency.registry, contingency.datetime, contingency.bc1, contingency.bc2, contingency.bc3, contingency.bc4, contingency.qtr1, contingency.qtr2, contingency.qtr3, contingency.qtr4))
            self.connection.commit()
            return True
        except Error as e:
            print('Error: ',e)
            return False
        
    # def listRegistry(self):
    #     try:
    #         sql = 'SELECT * FROM contingency'
    #         cursor = self.connection.cursor()
    #         cursor.execute(sql)
    #         for c in cursor:
    #             contingency = Contingency(c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10], c[11], c[12], c[13])
    #             list.append(contingency)
    #             return list
    #     except Error as e:
    #         print(e)
    #         return False
    
    def insertId(self):
        try:
            sql = 'SELECT idcontingency FROM contingency WHERE idcontingency = (SELECT MAX(idcontingency) FROM contingency)'
            cursor = self.connection.cursor()
            cursor.execute(sql)
            fet = cursor.fetchall()         
            fet2 = str(fet).strip('[]')
            fet3 = fet2.strip('()')
            fet4 = fet3.replace(',', '')
            return int(fet4) + 1
        except Error as e:
            print(e)
            return False