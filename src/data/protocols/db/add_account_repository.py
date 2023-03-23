
from abc import ABC, abstractmethod

class AddAccountRepository(ABC):
    
    @abstractmethod
    def sign_up(self, name: str, email: str, password: str) -> bool:
        raise (NotImplementedError)