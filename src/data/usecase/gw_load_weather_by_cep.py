
from src.data.protocols.gateway.inpe_gateway import InpeGateway
from src.data.protocols.gateway.via_cep_gateway import ViaCepGateway
from src.domain.usecase.load_weather_by_cep import LoadWeatherByCep


class GwLoadweatherByCep(LoadWeatherByCep):
    
    def __init__(
        self, 
        via_cep_gateway: ViaCepGateway,
        inpe_gateway: InpeGateway
    ):
        self.via_cep_gateway = via_cep_gateway
        self.inpe_gateway = inpe_gateway
    
    def load_weather(self, cep: str) -> dict:
        city_data = self.via_cep_gateway.city_search(cep)
        if not city_data:
            return None
        city_id = self.inpe_gateway.search_id_city(city_data['localidade'])
        
        if city_id:
            weather_data = self.inpe_gateway.search_weather_four_days(city_id)
            city_data.update(weather_data)
            
            return city_data
        city_data.setdefault("previsao", {})
        return city_data
        
            
    