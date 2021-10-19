from mysql.connector import Error
import mysql.connector

class Database:
  def __init__(self):
      pass
  
  def connect(self):
      server = 'localhost'
      user = 'root'
      password = '123456'
      db = 'db_pharmacy'
      try:
          self.connection = mysql.connector.connect(host=server, database=db, user=user, password=password)
          return True
      except Error as e:
          print('Error: ',e)
          return False
