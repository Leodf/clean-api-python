
from flask import current_app
from src.data.protocols.elasticsearch.log_repository import LogRepository


class ElasticLogRepository(LogRepository):

    def __init__(self):
        self.es_logger = current_app.extensions.get('elasticsearch_logger')

    def get_logs(self):
        search_body = {
            "size": 100,
            "sort": {
                "date" : {"order" : "desc"}  
            },
            "query": {
                "match_all": {}
            },
        }
        result = self.es_logger.es.search(index='logs', body=search_body)
        logs = [item['_source'] for item in result['hits']['hits']]

        return logs
