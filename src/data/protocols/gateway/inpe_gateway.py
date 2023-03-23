
from abc import ABC, abstractmethod

class InpeGateway(ABC):
    
    @abstractmethod
    def search_id_city(self, city: str) -> str:
        raise (NotImplementedError)
    
    @abstractmethod
    def search_weather_four_days(self, city_id: str) -> dict:
        raise (NotImplementedError)