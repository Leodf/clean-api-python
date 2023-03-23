
from abc import ABC, abstractmethod

class CheckAccountByEmailRepository(ABC):
    
    @abstractmethod
    def check_by_email(self, email: str) -> bool:
        raise (NotImplementedError)