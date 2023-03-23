
from abc import ABC, abstractmethod

class Hasher(ABC):
    
    @abstractmethod
    def hash(self, value: str) -> str:
        raise (NotImplementedError)