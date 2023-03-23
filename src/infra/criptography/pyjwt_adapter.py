from datetime import datetime
from jwt import encode, decode
from src.data.protocols.criptography.decrypter import Decrypter
from src.data.protocols.criptography.encrypter import Encrypter

class PyJwtAdapter(Encrypter, Decrypter):
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        
    def encrypt(self, value: str) -> str:
        access_token = encode(payload={ "id": value, "iat": datetime.now() }, key=self.secret_key)
        return access_token
    
    def decrypt(self, value: str) -> dict:
        decrypted_value = decode(value, self.secret_key, 'HS256')
        return decrypted_value
    
    