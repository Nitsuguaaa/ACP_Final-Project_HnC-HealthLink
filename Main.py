from Frontend import scrdir
from MySQL03 import sqldir

frontEnd = scrdir.ScrPages()
sql = sqldir.SqlCommands()

sql.dbBuilder()
frontEnd.loginscr()
