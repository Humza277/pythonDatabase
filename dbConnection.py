import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'


try:
    connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' + database +';UID='+ username +';PWD='+ password)
    print("Connection Established")
except:
    print("Did not connect")
else:
    pass

cursor = connections.cursor()


query1 = cursor.execute("SELECT * FROM Customers")
rows = query1.fetchone()
#print(type(rows))
#print(rows[1])
#print(rows.ContactName)
row1 = query1.fetchmany(30)
print(row1)

#print(query1)
#
# rows = cursor.fetchall()
for row in row1:
    print(row)

# assignment calculate the average of all the pro