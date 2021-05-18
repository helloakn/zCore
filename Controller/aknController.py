from zCore import Database, Table
from Model import User
class aknController():
    def __init__(self):
        print('hello xxxxx')

    def speak(parameters):

        return {
        "status_code": 200,
        "content_type":"text/html",
        "data":{
            "text" : "i'm speak function"
            }
        }

    def sayHi(parameters):
        #table = Table()
        #table.Select("id","name")
        #result = Database.select("select id,name from User")
        #user = User.Select('id','password').Where("id<>1").Get()
        #user = User.Select('id','password').Get()
        user = User.Select('id','name').OrderBy("id desc","name").Get()
        print(user)
        for x in user:
            print(x)
        return {
        "status_code": 200,
        "content_type":"text/html",
        "data":{
            "text" : "i'm sayHi function"
            }
        }
        
    