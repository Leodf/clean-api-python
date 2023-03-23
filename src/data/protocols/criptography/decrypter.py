
from abc import ABC, abstractmethod

class Decrypter(ABC):
    
    @abstractmethod
    def decrypt(self, value: str) -> dict:
        raise (NotImplementedError)