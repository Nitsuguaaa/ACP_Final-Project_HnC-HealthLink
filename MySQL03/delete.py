from MySQL03 import sqldir
def deletesql(table, element = None, value = None):
    sqlCom = sqldir.SqlCommands()
    mydb = sqlCom.initDB('healthlinkdb')

    mycursor = mydb.cursor()

    if element is None or value is None:
        mycursor.execute(f"DELETE FROM {table}")
        mydb.commit()
    else:
        mycursor.execute(f"DELETE FROM {table} WHERE {element} = '{value}'")
        mydb.commit()

    mydb.close()