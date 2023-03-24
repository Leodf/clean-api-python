import datetime
from click import DateTime
from flask import request
from src.data.protocols.elasticsearch.log_repository import LogRepository
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse


class LogControllerDecorator():
    def __init__(self, controller: Controller, log_repository: LogRepository):
        self.controller = controller
        self.log_repository = log_repository
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        response = self.controller.handle(http_request)
        data = datetime.datetime.now()
        doc = {
            "status_code": response['status_code'],
            "route": request.base_url,
            "method": request.method,
            "date": data
        }
        self.log_repository.save_log(index='log', id=request.method, body=doc)
            
        return response
    
        
        
        