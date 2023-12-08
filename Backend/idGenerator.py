import random
from MySQL03 import sqldir

sql = sqldir.SqlCommands()
def patientIDGenerator():
    patientID = "PT-" + str(random.randint(1111, 9999))

    IDList = sql.select("patienttbl", "patientID")

    if not IDList:
        return patientID
    else:
        for ID in IDList:
            if ID[0] == patientID:
                print("Patient ID already exists")
                patientIDGenerator()

                break
            else:
                return patientID