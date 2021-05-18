class Env():
    data = {}
    with open(".env", "r") as f:
        for x in f:
            x =  x.replace("\r", "")
            x =  x.replace("\n", "")
            raw = x.split("=")
            if(len(raw)==2):
                data[raw[0]] = raw[1]
            else:
                data[raw[0]] = None
    def __init__(self):
        print("Env Constructor")

    @staticmethod
    def get(key):
        if key in Env.data:
            return Env.data[key]
        else: return False
        
