from zCore import App
from Route import Route
import time

if __name__ == "__main__":  
    
    #route.Begin()
    hostName = "localhost"
    serverPort = 8080 
    app = App(hostName, serverPort)
    #SVR.route = "asdfasdfasdf"
    #print(SVR.getRoute())
    route = Route(app)
    #routeList = route.Begin(SVR)
    #print(SVR.route)
    svr = app.Star()
    