import mysql.connector
def insertsql(database, table, elements, values):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database=database)
    except:
        print('Failed to connect')
        exit()

    mycursor = mydb.cursor()

    command = f"INSERT INTO {table} ({elements}) VALUES ("
    for x in range(len(values)):
        if x == len(values)-1:
            command += "%s)"
        else:
            command += "%s, "

    mycursor.execute(command, values)

    mydb.commit()
    mydb.close()