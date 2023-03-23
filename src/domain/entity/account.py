
class AccountEntity:
    def __init__(self, id: str, name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.password = password
    
    def toJson(self):
        return self.__dict__
    