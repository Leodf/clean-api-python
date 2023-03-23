
from typing import Type
from src.domain.usecase.authentication import Authentication
from src.presentation.helpers.http_helpers import HttpHelpers
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse
from src.domain.usecase.add_account import AddAccount


class SignUpController(Controller):
   
   def __init__(
       self, 
       add_account: AddAccount,
       authentication: Authentication
    ):
        self.add_account = add_account
        self.authentication = authentication
   
   def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        try:
            body_params = http_request.body.keys()
            required_params = ["name", "email","password"]
            for param in required_params:
                if not param in body_params:
                    return HttpHelpers.bad_request('Missing Param Error')

            name = http_request.body["name"]
            email = http_request.body["email"]
            password = http_request.body["password"]
            isValid = self.add_account.sign_up(name, email, password)
            if not isValid:
                return HttpHelpers.forbidden('Email in use')
            authentication_model = self.authentication.auth(email, password)
            
            return HttpHelpers.ok(authentication_model)
             
        except Exception as exc:
            return HttpHelpers.server_error(exc)