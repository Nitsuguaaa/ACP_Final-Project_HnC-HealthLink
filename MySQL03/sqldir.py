from MySQL03 import select, insert

class SqlCommands:
    def select(self, database, table, column="*", constraints=None):
        return select.selectsql(database, table, column, constraints)
    def insert(self, database, table, elements, values):
        insert.insertsql(database, table, elements, values)