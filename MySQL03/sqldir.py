from MySQL03 import select, insert, delete, update, dbbuilder
import mysql.connector

class SqlCommands:
    def initDB(self, database):
        return dbbuilder.initDB(database)
    def select(self, table, column="*", constraints=None):
        return select.selectsql(table, column, constraints)
    def insert(self, table, elements, values):
        insert.insertsql(table, elements, values)
    def delete(self, table, element, value):
        delete.deletesql(table, element, value)
    def update(self, table, element, value, whereElement, whereValue):
        update.updatesql(table, element, value, whereElement, whereValue)
    def dbBuilder(self):
        dbbuilder.checkdb()