import sqlite3
conn= sqlite3.connect('database.db')
print('opened db seccesfully')
print('creating table')
conn.execute('CREATE TABLE survey(surname TEXT,fullname TEXT,contact TEXT,date TEXT,age INTEGER'
             ',pizza TEXT,pasta TEXT,pap TEXT,chicken TEXT,beef TEXT,other TEXT,'
             'movies TEXT,tv TEXT,radio TEXT,out TEXT'')')
print('table Created successfull')
print('clossing db')
conn.close()