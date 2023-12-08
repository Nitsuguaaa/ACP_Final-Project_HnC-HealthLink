from Frontend import scrdir
from Backend import backenddir
from MySQL03 import sqldir

frontEnd = scrdir.ScrPages()
sql = sqldir.SqlCommands()
backend = backenddir.backendCommands()

sql.dbBuilder()
frontEnd.loginscr()















'''
Hello World
from MySQL03 import sqldir
from Backend import backenddir

MySQL = sqldir.SqlCommands()
backEnd = backenddir.backendCommands()

    GUI Directory

frontEnd.loginscr()  # Opens login screen
frontEnd.homescr()  # Opens Home Screen


    SQL Directory

# Inserts user Maria into the users tbl table
MySQL.insert("hsptlpassworddb", "userstbl", "name, age, address", ("Maria", 19, "Balagtas, Batangas City"))
# shows the userstbl table (Other parameters that have defaults: column="*", constraints=None e.g."WHERE Username='Mark'")
MySQL.select("hsptlpassworddb", "userstbl")

    Backend Directory
# Input of application user, first parameter is Username and second is the password
backEnd.passwordCheck("Augustin", "pass123")
'''


