import mysql.connector
from zCore import Env
class Database():
    db = mysql.connector.connect(
        host=Env.get('DATABASE_SERVER'),
        user=Env.get('DATABASE_USER'),
        password=Env.get('DATABASE_PASSWORD'),
        database=Env.get('DATABASE_NAME'),
        auth_plugin='mysql_native_password'
    )
    dbCursor = db.cursor()

    def __init__(self, hostName, serverPort):
        self.hostName = hostName
        self.serverPort = serverPort
    
    @staticmethod
    def select(cmdString):
        Database.dbCursor.execute(cmdString)
        return Database.dbCursor.fetchall()