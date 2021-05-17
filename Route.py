class Route():
    def __init__(self,route):
        route.hello("zzzzz")
        #route.addRoute(requestMethod,requestURL,Controller,Function);
        route.addRoute('get','/d1','Controller.aknController','speak');
        
    