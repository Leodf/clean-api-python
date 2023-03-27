
from abc import ABC, abstractmethod


class LogRepository(ABC):
    
    @abstractmethod
    def get_logs(self) -> dict:
        raise (NotImplementedError)