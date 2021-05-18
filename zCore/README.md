# zCore Framework by AKN via Zote Innovation
## Run App
```
 python3 start.py
```

## File Structure
```
 [dir] Controller
    []...
 [dir] zCore # you have no permission to modify 
    
    []...
 [dir] Model
    [file] User.py
    [file] Admin.py
 [file] Route.py # all your request route here u go ;)
 [file] start.py # Start Up App Program
 [file] .env # configuration file, eng : db info, svr info (should be in .gitignore file) 
```

## Installation
### mysql
```
    python3 -m pip install mysql
    python3 -m pip install mysql-connector
```
### mysql-trouble shooting
You're using mysql_native_password, which is no longer the default. Assuming you're using the correct connector for your version you need to specify the auth_plugin argument when instantiating your connection object
```
cnx = mysql.connector.connect(user='haha', password='password',
                              host='127.0.0.1', database='test',
                              auth_plugin='mysql_native_password')
```
select Host,User,plugin from mysql.user;

| Host      | User                | plugin                |
|-----------|---------------------|-----------------------|
| %         | akn                 | mysql_native_password |
| %         | haha                | mysql_native_password |
| localhost | mysql.infoschema    | caching_sha2_password |
| localhost | mysql.session       | caching_sha2_password |
| localhost | mysql.sys           | caching_sha2_password |
| localhost | nativeuser          | mysql_native_password |
| localhost | root                | caching_sha2_password |

## Route

```
class Route():
   def __init__(self,route):
      route.addRoute('get','/d1','Controller.aknController','speak')
      route.addRoute('get','/sayinghi','Controller.aknController','sayHi')
        
      route.prefix('/test',
         Route.userRoute,
         Route.adminRoute,
      )
      route.addRoute('get','hello','Controller.aknController','speak')

    
   def userRoute(route):
      route.addRoute('get','user','Controller.aknController','speak')

   def adminRoute(route):
      route.addRoute('get','admin','Controller.aknController','speak')
      route.addRoute('get','admin/Login','Controller.aknController','speak')

```