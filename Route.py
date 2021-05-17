class Route():
    def __init__(self,route):
        #route.hello("zzzzz")
        #route.addRoute(requestMethod,requestURL,Controller,Function);
        route.addRoute('get','/d1','Controller.aknController','speak')
        
        route.prefix('test',
            self.userRoute(route)
        )
    def userRoute(self,route):
        print("hello this is userRoute")
        route.addRoute('get','/d1','Controller.aknController','speak')
        return "hello adfasd fasd fasdfas df asdf a"
        
        #route.addRoute('get','/d1','Controller.aknController','speak')
