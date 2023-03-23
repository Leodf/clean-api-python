from werkzeug.security import generate_password_hash, check_password_hash
from src.data.protocols.criptography.hash_comparer import HashComparer
from src.data.protocols.criptography.hasher import Hasher


class WerkzeugAdapter(Hasher, HashComparer):
    
    def __init__(self, salt: int):
        self.salt = salt
    
    def hash(self, value: str) -> str:
        hashing = generate_password_hash(value, salt_length=self.salt)
        return hashing
    
    def compare(self, hash: str, value: str) -> bool:
        is_valid = check_password_hash(hash, value)
        return is_valid