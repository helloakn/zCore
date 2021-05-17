from zCore import APP
from Route import Route
import time

if __name__ == "__main__":  
    
    #route.Begin()
    hostName = "localhost"
    serverPort = 8080 
    app = APP(hostName, serverPort)
    #SVR.route = "asdfasdfasdf"
    #print(SVR.getRoute())
    route = Route(app)
    #routeList = route.Begin(SVR)
    #print(SVR.route)
    app = app.Star()
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        app.serve_forever()
    except KeyboardInterrupt:
        pass

    app.server_close()
    print("Server stopped.")