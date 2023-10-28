import mysql.connector
def selectsql(dbname):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database=dbname)
    except:
        print('Failed to connect')
        exit()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM testTBL")
    myresult = mycursor.fetchall()

    mylist = []
    for x in myresult:
        mylist.append(x)

    mydb.close()
    return mylist
