from zCore import App,Env
from Route import Route
import time

if __name__ == "__main__":  
    db_user = Env.get('db_user')
    print(db_user)
    
    #route.Begin()
    hostName = Env.get('WEB_SVR_IP') 
    serverPort = Env.get('WEB_SVR_PORT') 
    app = App(hostName, int(serverPort))
    #SVR.route = "asdfasdfasdf"
    #print(SVR.getRoute())
    route = Route(app)
    #routeList = route.Begin(SVR)
    #print(SVR.route)
    svr = app.Star()
    