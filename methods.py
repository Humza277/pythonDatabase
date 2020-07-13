from db2 import *


def enterSQL(self, command):
    return self.cursor.execute(command)


def avgprice(self):
    # calc avg unit price of all the products
    return self.enterSQL("SELECT AVG(UnitPrice) FROM Products").fetchone()


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

def avgprice():
    db = Database()
    print(db.avgprice())


# test()
avgprice()
