from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):
    routeList = []
    #def __init__(self):
        #print('starting')
        #app.addRoute('get','/d1','Controller.aknController','speak')
        #print(app.routeList)
        #print("hello testing 1 2 3 3")
        #self.routeList = routeList

    def do_GET(self):
        #print('hello');
        #print("this is fucking path"+self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
