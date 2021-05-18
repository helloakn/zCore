from zCore import Env
from .Database import Database
class Table():

    fields = {}
    softDelete = True

    selectColumns = ""
    tableName = ""
    whereCase = ""
    orderCase = ""
    groupCase = ""
    

    def __init__(self):
        self.selectColumns = ""
        self.tableName = ""
        self.whereCase = ""
        self.orderCase = ""
        self.groupCase = ""
        
    @staticmethod
    def Get():
        #cmdString = Table.selectColumns + (Table.whereCase==""?"":" WHERE "+Table.whereCase)
        #WHERE 
        cmdString = Table.selectColumns + ("" if Table.whereCase=="" else " WHERE "+Table.whereCase)
        #ORDER 
        cmdString = cmdString + ("" if Table.orderCase=="" else " ORDER BY "+Table.orderCase)
        #print(cmdString)
        Database.dbCursor.execute(cmdString)
        return Database.dbCursor.fetchall()
        
    @staticmethod
    def OrderBy(*orderCase):
        Table.orderCase = ",".join(str(x) for x in orderCase)
        return Table

    @staticmethod
    def Where(wCase):
        Table.whereCase += wCase
        return Table
        
    @staticmethod
    def Select(*col):
        Table.selectColumns = "SELECT "+",".join(str(x) for x in col) + " FROM " +Table.tableName
        return Table
        #Database.dbCursor.execute(cmdString)
        #return Database.dbCursor.fetchall()
