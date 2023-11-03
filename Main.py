from Frontend import scrdir
from MySQL03 import sqldir
from Backend import backenddir

frontEnd = scrdir.ScrPages()
MySQL = sqldir.SqlCommands()
backEnd = backenddir.backendCommands()

frontEnd.loginscr()
# print(MySQL.select("hsptlpassworddb", "userstbl"))
# backEnd.passwordCheck("Augustin", "pass123")

