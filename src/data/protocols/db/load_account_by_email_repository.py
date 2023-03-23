
from abc import ABC, abstractmethod

from src.domain.entity.account import AccountEntity

class LoadAccountByEmailRepository(ABC):
    
    @abstractmethod
    def load_by_email(self, email: str) -> dict:
        raise (NotImplementedError)