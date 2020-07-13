import secretFile
import pyodbc
import sys

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
        except pyodbc.InterfaceError:
            print("Did not connect")
            self.__exit__(sys.exc_info())

    def enterSQL(self, command):
        return self.cursor.execute(command)

    def avgprice(self):
        # calc avg unit price of all the products
        return self.enterSQL("SELECT AVG(UnitPrice) FROM Products").fetchone()

    def __exit__(self, exc_msg):
        print("__exit__")
        print(exc_msg)
        self.cursor.close()
        self.connections.close()

def test():
    try:
        command = input("please input sql command")
        db = Database()
        rows = db.enterSQL(command).fetchmany(30)
        for r in rows:
            print(r)
    except pyodbc.ProgrammingError:
        print("Command is incorrect")

# good to have generaised exceptiuons
# move the mothods to another class

def avgprice():
    db = Database()
    print(db.avgprice())

#test()
avgprice()
