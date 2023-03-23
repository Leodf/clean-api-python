
from abc import ABC, abstractmethod

class LoadWeatherByCep(ABC):
    
    @abstractmethod
    def load_weather(self, cep: str) -> dict:
        raise (NotImplementedError)