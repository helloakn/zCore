from http.server import BaseHTTPRequestHandler, HTTPServer

class WebServer(BaseHTTPRequestHandler):
    def __init__(self,routeList):
        print("hello testing 1 2 3 3")
        print(routeList)
    def do_GET(self):
        print('hello');
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
