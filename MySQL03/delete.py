from MySQL03 import sqldir
def deletesql(table, element, value):
    sqlCom = sqldir.SqlCommands()
    mydb = sqlCom.initDB('healthlinkdb')

    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM {table} WHERE {element} = '{value}'")
    mydb.commit()

    mydb.close()