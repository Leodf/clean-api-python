import requests
from src.data.protocols.converter.converter_xml_to_dict import ConverterXmlToDict

from src.data.protocols.gateway.inpe_gateway import InpeGateway

class InpeApi(InpeGateway):
    _url_base = 'http://servicos.cptec.inpe.br'
    
    def __init__(self, converter_xml_to_dict: ConverterXmlToDict):
        self.converter_xml_to_dict = converter_xml_to_dict
    
    def search_id_city(self, city: str) -> str:
        payload = { 'city': city }
        url = f"{self._url_base}/XML/listaCidades"
        response = requests.get(url, params=payload)
        response_dict = self.converter_xml_to_dict.converter(response.text)
        city_id = response_dict['cidades']['cidade']['id']
        return city_id
    
    def search_weather_four_days(self, city_id: str) -> dict:
        url = f"{self._url_base}/XML/cidade/{city_id}/previsao.xml"
        response = requests.get(url)
        response_dict = self.converter_xml_to_dict.converter(response.text)
        format_weather_data = {}
        format_weather_data.update(response_dict['cidade'])
        format_weather_data.pop('nome')
        return format_weather_data
    
    