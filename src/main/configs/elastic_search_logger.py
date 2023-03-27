import logging
from datetime import datetime
import os
from elasticsearch import Elasticsearch
from flask import request

class ElasticSearchLogger():
 
    def __init__(self, index_name, elasticsearch_host):
        self.es = Elasticsearch([elasticsearch_host])
        self.index_name = index_name
        
    def init_app(self, app):
        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions['elasticsearch_logger'] = self
    
    def log(self, level, message):
        document = {
            'date': datetime.now(),
            'level': level,
            'url': request.base_url,
            'method': request.method,
            'message': message,
            'logger': self.index_name
        }
        self.es.index(index=self.index_name, body=document)

    def info(self, message):
        self.log(logging.INFO, message)
    
    def warning(self, message):
        self.log(logging.WARNING, message)

    def error(self, message, extra=None):
        self.log(logging.ERROR, message)

    def critical(self, message, extra=None):
        self.log(logging.CRITICAL, message)

def init_app(app):
    elastic_url = os.environ.get('ELASTIC_URL') or 'http://localhost:9200'
    app.config.setdefault('ELASTIC_URL', elastic_url)
    es_logger = ElasticSearchLogger('logs', app.config['ELASTIC_URL'])
    es_logger.init_app(app)

  