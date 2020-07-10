import pyodbc
import secretFile
import sys

class Database:


    def __init__(self):
        try:
            self.connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server +
                                              ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            print("Connection Established")
        except Exception:
            self.__exit__(sys.exc_info())
            print("Did not connect")

        self.cursor = self.connection.cursor()

    def enter(self, command):


    def __exit__(self, exc_msg):
        print("__exit__")
        print(exc_msg)
        self.cursor.close()
        self.connections.close()







cursor = connections.cursor()
query1 = cursor.execute("SELECT * FROM Customers")
rows = query1.fetchone()
# print(type(rows))
# print(rows[1])
# print(rows.ContactName)
row1 = query1.fetchmany(30)
print(row1)

# print(query1)
#
# rows = cursor.fetchall()
for row in row1:
    print(row)

# assignment calculate the average of all the pro
# presentation how you have designed it after exam start working on the design
