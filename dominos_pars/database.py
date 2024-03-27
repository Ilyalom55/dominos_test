import sqlite3

sql = 'CREATE TABLE menu (name TEXT, description TEXT, price TEXT)'
sql_data = 'SELECT * FROM menu'
connect = sqlite3.connect('menu.db')

cursor = connect.cursor()

cursor.execute(sql_data)

res = cursor.fetchall()

for r in res:
    print('Name:', r[0])
    print('Description:', r[1])
    print('Price:', r[2])

connect.close()