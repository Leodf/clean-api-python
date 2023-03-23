import re
from typing import Type
from src.domain.usecase.authentication import Authentication
from src.domain.usecase.load_weather_by_cep import LoadWeatherByCep
from src.presentation.helpers.http_helpers import HttpHelpers
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse


def is_valid_cep(cep):
    if len(cep) == 8:
        cep_pattern = re.compile(r'(\d){5}(\d){3}')
        cep_pattern.match(cep)
        return True
    else:
        return False

class LoadWeatherController(Controller):

    def __init__(
        self,
        load_weather_data: LoadWeatherByCep
    ):
        self.load_weather_data = load_weather_data

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        try:
            body_params = http_request.body.keys()
            if not "cep" in body_params:
                return HttpHelpers.bad_request('Missing Param Error')

            cep = http_request.body["cep"]
            is_valid = is_valid_cep(cep)
            if not is_valid:
                return HttpHelpers.bad_request('cep inválido')
            weather_data = self.load_weather_data.load_weather(cep)
            if not weather_data:
                return HttpHelpers.bad_gateway('city not found')

            return HttpHelpers.ok(weather_data)

        except Exception as exc:
            return HttpHelpers.server_error(exc)
