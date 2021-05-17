# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from .WebService import WebServer

class Test():
    def testing(self):
        print('hello')

class APP():
    route = None
    def __init__(self, hostName, serverPort):
        self.hostName = hostName
        self.serverPort = serverPort

    def hello(self,text):
        self.route = text

    def Star(self):
        webServer = WebServer(self.route);
        self.SVR = HTTPServer((self.hostName, self.serverPort), webServer)
        return self.SVR 

    def addRoute(self,requestMethod,requestURL,Controller,Function):
        #print(requestMethod)
        #print(requestURL)
        print(Controller)
        print(Function)

        objFunction = self.modLoader(Controller+"."+Function)
        some_object = objFunction("hello world")

    def modLoader(self,name):
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod
    def getRoute(self):
        return self.route
        
