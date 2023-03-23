from typing import Type
from abc import ABC, abstractmethod
from .http import HttpRequest, HttpResponse

class Controller(ABC):
    
    @abstractmethod
    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise (NotImplementedError)