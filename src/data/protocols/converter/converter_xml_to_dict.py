
from abc import ABC, abstractmethod


class ConverterXmlToDict(ABC):
    
    @abstractmethod
    def converter(self, xml: str) -> dict:
        raise (NotImplementedError)