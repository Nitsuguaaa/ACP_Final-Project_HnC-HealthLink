import mysql.connector
def updatesql(database, table, element, value, whereElement, whereValue):
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="", database=database)
    except:
        print('Failed to connect')
        exit()

    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE {table} SET {element} = '{value}' WHERE {whereElement} = '{whereValue}'")
    mydb.commit()