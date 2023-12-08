from MySQL03 import select, insert, delete, update, dbbuilder
import mysql.connector

class SqlCommands:
    def initDB(self, database):
        return dbbuilder.initDB(database)
    def select(self, table, column="*", constraints=None, fetchOne=False):
        return select.selectsql(table, column, constraints, fetchOne)
    def insert(self, table, elements, values):
        insert.insertsql(table, elements, values)
    def delete(self, table, element = None, value = None):
        delete.deletesql(table, element, value)
    def update(self, table, element, value, whereElement, whereValue):
        update.updatesql(table, element, value, whereElement, whereValue)
    def dbBuilder(self):
        dbbuilder.checkdb()