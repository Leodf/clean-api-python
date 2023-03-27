import datetime
from click import DateTime
from flask import request
from src.data.protocols.elasticsearch.log_repository import LogRepository
from src.presentation.helpers.http_helpers import HttpHelpers
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse


class LogController(Controller):
    def __init__(self, log_repository: LogRepository):
        self.log_repository = log_repository
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            logs = self.log_repository.get_logs()
            return HttpHelpers.ok(logs)
        except Exception as exc:
            return HttpHelpers.server_error(exc)
    
        
        
        