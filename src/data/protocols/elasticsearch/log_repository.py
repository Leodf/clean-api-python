
from abc import ABC, abstractmethod


class LogRepository(ABC):
    
    @abstractmethod
    def save_log(self, index: str, id: str, body: dict) -> None:
        raise (NotImplementedError)