
from flask import current_app
from src.data.protocols.elasticsearch.log_repository import LogRepository


class ElasticLogRepository(LogRepository):
    
    def __init__(self):
        self.es = current_app.extensions['elasticsearch'].get_connection()
        
    def save_log(self, index: str, id: str, body: dict):
        self.es.index(index=index, id=id, body=body)
        
    def load_logs(self, index: str, param: str):
        raise (NotImplementedError)