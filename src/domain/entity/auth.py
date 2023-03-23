
class AuthEntity:
    def __init__(self, access_token: str, name: str):
        self.access_token = access_token
        self.name = name
    
    def toJson(self):
        return self.__dict__