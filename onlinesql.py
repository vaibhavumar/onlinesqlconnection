import mysql.connector

db = mysql.connector.connect(host="www.db4free.net", port=3306, user="vaibhav", passwd="12345678", database="my_database")

cur = db.cursor()
cur.execute("DESC tb1")
result = cur.fetchall()
print(cur.columnnames)
for x in result:
	print(x[0],x[1],x[2],x[3],x[4],x[5],sep=' ')