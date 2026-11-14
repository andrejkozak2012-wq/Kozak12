import sqlite3

connection = sqlite3.connect("itstep_DB.s13", 5)
cur = connection.cursor()

cur.execute("UPDATE first_table SET name= 'Dima' WHERE rowid=2;")
connection.commit()

res = cur.fetchall()
print(res)
connection.close()