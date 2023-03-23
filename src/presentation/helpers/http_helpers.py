from src.presentation.protocols.http import HttpResponse

class HttpHelpers:
    
    @staticmethod
    def ok(data: any) -> HttpResponse:
        return {
            "status_code": 200, 
            "body": data
        }
        
    @staticmethod
    def bad_request(error: any) -> HttpResponse:
        return {
            "status_code": 400, 
            "body": error
        }
        
    @staticmethod
    def forbidden(error: any) -> HttpResponse:
        return {
            "status_code": 403, 
            "body": error
        }

    @staticmethod
    def unauthorized():
        return {
            "status_code": 401, 
            "body": 'Unauthorized'
        }

    @staticmethod
    def server_error(error: any):
        return {
            "status_code": 500, 
            "body": error
        }
        
    @staticmethod
    def bad_gateway(error: any):
        return {
            "status_code": 504, 
            "body": error
        }