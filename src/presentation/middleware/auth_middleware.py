
from typing import Type
from src.domain.usecase.load_account_by_token import LoadAccountByToken
from src.presentation.helpers.http_helpers import HttpHelpers
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse


class AuthMiddleware(Controller):
   
   def __init__(
       self, 
       load_account_by_token: LoadAccountByToken
    ):
        self.load_account_by_token = load_account_by_token
   
   def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        
        access_token = http_request.headers.get('X-Access_token')
        try:
            if access_token:
                accountId = self.load_account_by_token.load_by_token(access_token)
                if accountId:
                    return HttpHelpers.ok({"id": accountId})
            
            return HttpHelpers.forbidden('Access denied')
             
        except Exception as exc:
            return HttpHelpers.server_error(exc)