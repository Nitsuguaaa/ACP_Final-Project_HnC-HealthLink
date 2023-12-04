import mysql.connector

def initDB(database = None):
    try:
        if database is None:
            mydb = mysql.connector.connect(host="localhost", user="root", password="")
        else:
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database=database)
    except:
        print('Failed to connect')
        exit()
    return mydb

def checkdb():
    mydb = initDB()
    HealthLinkDB = False

    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        if x[0] == "healthlinkdb":
            HealthLinkDB = True

    if HealthLinkDB is False:
        mycursor.execute("CREATE DATABASE healthlinkdb")
        createAllTables()

    mydb.close()

def createAllTables():
    mydb = initDB("healthlinkdb")

    mycursor = mydb.cursor()

    tables = (
        "userlogintbl(username VARCHAR(255), password VARCHAR(30))",
        "patienttbl(patientID VARCHAR(7) NOT NULL , patientName VARCHAR(255), patientAddress VARCHAR(255), PRIMARY KEY (patientID))",
        "patientinfotbl(patientID VARCHAR(7), patientDisease VARCHAR(255), patientIn DATE, patientOut DATE, FOREIGN KEY (patientID) REFERENCES patienttbl(patientID))",
        "topdiseasetbl(disease VARCHAR(255))",
        "topaddresstbl(address VARCHAR(255))"
    )

    for x in tables:
        print("CREATE TABLE", x)
        mycursor.execute("CREATE TABLE " + x)

    mydb.close()