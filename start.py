from zCore import APP
from Route import Route
import time

if __name__ == "__main__":  
    
    #route.Begin()
    hostName = "localhost"
    serverPort = 8080 
    SVR = APP(hostName, serverPort)
    #SVR.route = "asdfasdfasdf"
    #print(SVR.getRoute())
    route = Route(SVR)
    #routeList = route.Begin(SVR)
    print(SVR.route)
    SVR = SVR.Star()
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        SVR.serve_forever()
    except KeyboardInterrupt:
        pass

    SVR.server_close()
    print("Server stopped.")