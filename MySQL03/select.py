import mysql.connector
def selectsql(database, table, column="*", constraints=None):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database=database)
    except:
        print('Failed to connect')
        exit()

    mycursor = mydb.cursor()
    if constraints is None:
        mycursor.execute(f"SELECT {column} FROM {table}")
    else:
       mycursor.execute(f"SELECT {column} FROM {table} {constraints}")

    tableResult = mycursor.fetchall()

    results = []
    for x in tableResult:
        results.append(x)

    mydb.close()
    return results
