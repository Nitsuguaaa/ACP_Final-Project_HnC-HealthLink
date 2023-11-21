from MySQL03 import select, insert, delete, update

class SqlCommands:
    def select(self, database, table, column="*", constraints=None):
        return select.selectsql(database, table, column, constraints)
    def insert(self, database, table, elements, values):
        insert.insertsql(database, table, elements, values)
    def delete(self, database, table, element, value):
        delete.deletesql(database, table, element, value)
    def update(self, database, table, element, value, whereElement, whereValue):
        update.updatesql(database, table, element, value, whereElement, whereValue)