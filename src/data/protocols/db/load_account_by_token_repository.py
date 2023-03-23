
from abc import ABC, abstractmethod

class LoadAccountByTokenRepository(ABC):
    
    @abstractmethod
    def load_by_token(self, access_token: str) -> str:
        raise (NotImplementedError)