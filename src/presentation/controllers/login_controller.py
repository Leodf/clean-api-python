
from typing import Type
from src.domain.usecase.authentication import Authentication
from src.presentation.helpers.http_helpers import HttpHelpers
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse


class LoginController(Controller):
   
   def __init__(
       self, 
       authentication: Authentication
    ):
        self.authentication = authentication
   
   def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        try:
            body_params = http_request.body.keys()
            required_params = ["email","password"]
            for param in required_params:
                if not param in body_params:
                    return HttpHelpers.bad_request('Missing Param Error')

            email = http_request.body["email"]
            password = http_request.body["password"]
            authentication_model = self.authentication.auth(email, password)
            if not authentication_model:
                return HttpHelpers.unauthorized()
            
            return HttpHelpers.ok(authentication_model)
             
        except Exception as exc:
            return HttpHelpers.server_error(exc)