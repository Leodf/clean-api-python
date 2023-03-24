
class AuthEntity:
    def __init__(self, access_token: str, id: str):
        self.access_token = access_token
        self.id = id
    
    def toJson(self):
        return self.__dict__