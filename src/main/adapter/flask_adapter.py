from typing import Type
from src.presentation.protocols.controller import Controller
from src.presentation.protocols.http import HttpRequest, HttpResponse

def flask_adapter(request: any, api_controller: Type[Controller]) -> any:
    if request.method == 'GET':
        body = None
    else:
        body = request.json
    
    http_request = HttpRequest(
        headers=request.headers, body=body, query=request.args
    )
    response = api_controller.handle(http_request)
    
    if response['status_code'] < 299:
        return {
            "message": response['body'],
            "status_code": response['status_code']
        }, response['status_code']
    
    return {
        "error": response['body'],
        "status_code": response['status_code']
    }, response['status_code']
