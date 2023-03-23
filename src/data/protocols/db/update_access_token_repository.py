
from abc import ABC, abstractmethod

from src.domain.entity.account import AccountEntity

class UpdateAccessTokenRepository(ABC):
    
    @abstractmethod
    def update_access_token(self, id: str, token: str) -> None:
        raise (NotImplementedError)