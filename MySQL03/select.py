from MySQL03 import sqldir
def selectsql(table, column="*", constraints=None, fetchOne=False):
    sqlCom = sqldir.SqlCommands()
    mydb = sqlCom.initDB('healthlinkdb')

    mycursor = mydb.cursor()
    if fetchOne is False:
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
    else:
        if constraints is None:
            mycursor.execute(f"SELECT {column} FROM {table}")
        else:
            mycursor.execute(f"SELECT {column} FROM {table} {constraints}")
        tableResult = mycursor.fetchone()
        return tableResult
