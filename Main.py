import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="testDB")
except:
    print('Failed to connect')
    exit()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM testTBL")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mydb.close()