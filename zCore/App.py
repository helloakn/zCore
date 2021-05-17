
from http.server import BaseHTTPRequestHandler, HTTPServer
from .WebService import WebServer

class App():
    route = None
    routeList = []
    routePrefix = ""

    def __init__(self, hostName, serverPort):
        self.hostName = hostName
        self.serverPort = serverPort

    def getRouteList(self):
        return self.routeList

    
    def checkRoute(self,reqUrl):
        #print("this is is fucking request -> " + reqUrl)
        parameters = None
        print("xxxxx all route xxxxx")
        print(self.routeList)
        print('end all route')
        for rURL in self.routeList:
            #print(rURL[1])
            original_urls = rURL[1].split("/")
            request_urls = reqUrl.split("/")
            print("org and req url")
            print(original_urls)
            print(request_urls)
            print("=x=")
            if(len(original_urls )==len(request_urls)):
                tf = True;
                #foreach($original_urls as $ok=>$ov){
                oURLINdex = 0
                index = 0;
                while oURLINdex < len(original_urls):
                    oURL = original_urls[oURLINdex]
                #for oURL in original_urls:
                    #if(oURLINdex!=0):
                    searchWord = original_urls[oURLINdex]
                    isParameter = searchWord.find("{")
                    
                    if (isParameter == -1):
                        if(original_urls[oURLINdex] !=  request_urls[oURLINdex]  ):
                            tf = False;
                    else:
                        par = original_urls[oURLINdex].replace("{","")
                        par = par.par("}","")

                        parameters[par] = request_urls[oURL]
                    oURLINdex += 1
                #print("tf is ")
                #print(reqUrl)
                #print(tf)
                #print ("end tf")
                if(tf):
                    ttff = True
                    return self.goRoute(rURL,parameters)
                    break
                else:
                    ttff = False
        return False
    def goRoute(self,rURL,parameters):
        #print("fadsfasdfasd fasd fas df asdf asd fa +> => ")
        print(rURL[2])
        controller = rURL[2]
        function = rURL[3]
        objFunction = self.modLoader(controller+"."+function)
        return objFunction(parameters)
    def Star(self):
        routeList = self.routeList
        app = self
        #webServer = WebServer(self.route)
        #webServer = WebServer(self.routeList)
        class WebServer(BaseHTTPRequestHandler):
            def do_GET(self):
                #print('hello');
                print("this is fucking path => "+self.path)
                requestPath = self.path.split("?")[0];
                result = app.checkRoute(requestPath)
                if(result):
                    self.send_response(result['status_code'])
                    self.send_header("Content-type", result['content_type'])
                    self.end_headers()
                    self.wfile.write(bytes(result['data']['text'], "utf-8"))
                else:
                    self.send_response(404)
                    self.send_header("Content-type", 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes("Not FOund", "utf-8"))
                

        self.SVR = HTTPServer((self.hostName, self.serverPort), WebServer)
        print("Server started http://%s:%s" % (self.hostName, self.serverPort))

        try:
            self.SVR.serve_forever()
        except KeyboardInterrupt:
            print("fucking error")
            pass

        self.SVR.server_close()
        print("Server stopped.")

    def addRoute(self,requestMethod,requestURL,Controller,Function):
        #print("add route")
        #print(requestMethod)
        #print(requestURL)
        #print(Controller)
        #print(Function)
        self.routeList.append([requestMethod,self.routePrefix+requestURL,Controller,Function]);
        #objFunction = self.modLoader(Controller+"."+Function)
        #some_object = objFunction("hello world")

    def modLoader(self,name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod
    def getRoute(self):
        return self.route
    def prefix(self,prefixName,*customRoute):
        #print("prefix")
        self.routePrefix = prefixName
        for f in customRoute:
            f(self)
        self.routePrefix = ""
        #customRoute(self)
        #print('Fucking PRefix => '+prefixName)
        #print("fucking route -> "+str(self.route))
        #print(customRoute)
        #print("And all the rest... %s" % list(routelist))

