from MySQL03 import sqldir
def insertsql(table, elements, values):
    sqlCom = sqldir.SqlCommands()
    mydb = sqlCom.initDB('healthlinkdb')

    mycursor = mydb.cursor()

    command = f"INSERT INTO {table} ("
    for x in range(len(elements)):
        if x == len(elements)-1:
            command += (elements[x] + ")")
        else:
            command += (elements[x] + ", ")

    command += " VALUES ("
    for x in range(len(values)):
        if x == len(values)-1:
            command += "%s)"
        else:
            command += "%s, "

    print(command)

    mycursor.execute(command, values)

    mydb.commit()
    mydb.close()