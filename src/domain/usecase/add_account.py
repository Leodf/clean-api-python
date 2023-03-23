
from abc import ABC, abstractmethod

class AddAccount(ABC):
    
    @abstractmethod
    def sign_up(self, name: str, email: str, password: str) -> bool:
        raise (NotImplementedError)