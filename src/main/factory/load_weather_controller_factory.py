from src.data.usecase.gw_load_weather_by_cep import GwLoadweatherByCep
from src.infra.gateway.inpe_api import InpeApi
from src.infra.gateway.via_cep_api import ViaCepApi
from src.infra.xml_to_dict.xml_to_dict_adapter import XmlToDictAdapter
from src.presentation.controllers.load_weather_controller import LoadWeatherController
from src.presentation.protocols.controller import Controller

def load_weather_controller_factory() -> Controller:
    
    converter_xml_to_dict = XmlToDictAdapter()
    via_cep_gateway = ViaCepApi()
    inpe_gateway = InpeApi(converter_xml_to_dict)
    load_weather_data = GwLoadweatherByCep(via_cep_gateway, inpe_gateway)
    login_controller_factory = LoadWeatherController(load_weather_data)
    
    return login_controller_factory