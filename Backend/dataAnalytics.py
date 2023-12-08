from MySQL03 import sqldir
from collections import Counter

sql = sqldir.SqlCommands()

class dataAnalysis:
    def topAddress(self):
        addressList = sql.select("patienttbl", "patientBarangay")
        addressCount = Counter(addressList)

        sql.delete("topaddresstbl")

        for address in addressCount.most_common(3):
            print(address)
            sql.insert("topaddresstbl", ("address", "count"), (address[0][0], address[1]))

    def topDisease(self):
        topAddress = sql.select("topaddresstbl", column="MAX(address)")
        diseaseList = []

        sql.delete("topdiseasetbl")

        patients = sql.select("patienttbl", "patientID", f"WHERE patientBarangay = '{topAddress[0][0]}'")
        for getDisease in patients:
            data = sql.select("patientinfotbl", "patientDisease", constraints=f"WHERE patientID='{getDisease[0]}'")
            diseaseList.append(data[0][0])

        diseaseCount = Counter(diseaseList)

        for disease in diseaseCount.most_common(3):
            sql.insert("topdiseasetbl", ("disease", "count"), (disease[0], 1))
