
from abc import ABC, abstractmethod

class HashComparer(ABC):
    
    @abstractmethod
    def compare(self, hash: str, value: str) -> bool:
        raise (NotImplementedError)