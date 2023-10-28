import MySQL03.select as my

database = "testDB"

mylist = my.selectsql(database)

row = len(mylist)
col = len(mylist[0])

for x in range(row):
    for y in range(col):
        print(mylist[x][y], "\t\t", end="")
    print("")