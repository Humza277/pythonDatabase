from db2 import *
import pyodbc
import sys


def enterSQL(self, command):
    return self.cursor.execute(command)


# Calculates the average price
def avgprice(self):
    # calc avg unit price of all the products
    return self.enterSQL("SELECT AVG(UnitPrice) FROM Products").fetchone()


# adds SQL user commands to the cursor object
def test():
    try:
        command = input("please input sql command")
        db = Database()
        rows = db.enterSQL(command).fetchmany(30)
        for r in rows:
            print(r)
    except pyodbc.ProgrammingError:
        print("Command is incorrect")


# good to have generalized exceptions
# move the methods to another class

# gets the average price
def avgprice():
    db = Database()
    print(db.avgprice())


# Calls the methods
test()
avgprice()
