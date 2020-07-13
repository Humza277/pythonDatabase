import secretFile
import pyodbc
import sys
from methods import *

class Database:
    server = secretFile.server
    database = secretFile.database
    username = secretFile.username
    password = secretFile.password

    def __init__(self):
        try:
            self.connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +
                                              ';DATABASE=' + self.database + ';UID=' + self.username +
                                              ';PWD=' + self.password)
            print("Connection Established")
            self.cursor = self.connections.cursor()
        except Exception:
            print("Did not connect")
            self.__exit__(sys.exc_info())

    def __exit__(self, exc_msg):
        print("__exit__")
        print(exc_msg)
        self.cursor.close()
        self.connections.close()


