import mysql.connector

mydb = mysql.connector.connect(host="localhost",username = "root",password = "", database = "uidbytes")
mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM cards")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
