
from abc import ABC, abstractmethod


class ViaCepGateway(ABC):
    
    @abstractmethod
    def city_search(self, cep: str) -> dict:
        raise (NotImplementedError)