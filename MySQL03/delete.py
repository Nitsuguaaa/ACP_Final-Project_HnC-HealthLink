import mysql.connector
def deletesql(database, table, element, value):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database=database)
    except:
        print('Failed to connect')
        exit()

    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM {table} WHERE {element} = '{value}'")
    mydb.commit()