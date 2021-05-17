class Route():
    def __init__(self,route):
        #route.hello("zzzzz")
        #route.addRoute(requestMethod,requestURL,Controller,Function);
        route.addRoute('get','/d1','Controller.aknController','speak')
        route.addRoute('get','/sayinghi','Controller.aknController','sayHi')
        
        #route.prefix('test',
        #    self.userRoute(route)
        #)
        route.prefix('/test',
           Route.userRoute,
           
        )
        route.addRoute('get','hello','Controller.aknController','speak')

    def adminRoute(route):
        #print("hello this is userRoute")
        route.addRoute('get','admin','Controller.aknController','speak')
        route.addRoute('get','admin/Login','Controller.aknController','speak')

    def userRoute(route):
        #print("hello this is userRoute")
        route.addRoute('get','user','Controller.aknController','speak')
        #return "hello adfasd fasd fasdfas df asdf a"
        
        #route.addRoute('get','/d1','Controller.aknController','speak')
