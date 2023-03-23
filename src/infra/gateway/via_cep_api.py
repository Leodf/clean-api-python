import requests
from src.data.protocols.gateway.via_cep_gateway import ViaCepGateway

class ViaCepApi(ViaCepGateway):
    _url_base = 'https://viacep.com.br'
        
    def city_search(self, cep: str) -> dict:
        url = f"{self._url_base}/ws/{cep}/json/"
        data = dict(requests.get(url).json())
        return data
    
    