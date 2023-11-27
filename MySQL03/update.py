from MySQL03 import sqldir
def updatesql(table, element, value, whereElement, whereValue):
    sqlCom = sqldir.SqlCommands()
    mydb = sqlCom.initDB('healthlinkdb')

    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE {table} SET {element} = '{value}' WHERE {whereElement} = '{whereValue}'")
    mydb.commit()

    mydb.close()