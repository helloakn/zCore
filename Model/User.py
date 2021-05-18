from zCore import Database
from zCore import Table
class User(Table):
    Table.tableName = "USER"
    Table.fields = {}
    Table.softDelete = True
    def __init__(self):
        print("ok")
