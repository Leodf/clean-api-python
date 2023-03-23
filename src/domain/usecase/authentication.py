
from abc import ABC, abstractmethod

from src.domain.entity.auth import AuthEntity

class Authentication(ABC):
    
    @abstractmethod
    def auth(self, email: str, password: str) -> AuthEntity:
        raise (NotImplementedError)