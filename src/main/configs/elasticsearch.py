from elasticsearch import Elasticsearch

class ElasticsearchConnection:
    def __init__(self, uri, port):
        self._uri = uri
        self._port = port
        self._elasticsearch = None

    def init_app(self, app):
        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions['elasticsearch'] = self

    def open_connection(self):
        self._elasticsearch = Elasticsearch([{'host': self._uri, 'port': self._port, 'scheme': 'http'}])
    def get_connection(self):
        if self._elasticsearch is None:
            self.open_connection()
        return self._elasticsearch

    def close_connection(self):
        if self._elasticsearch:
            self._elasticsearch.close()

def init_app(app):
    app.config.setdefault('ELASTICSEARCH_URI', 'localhost')
    app.config.setdefault('ELASTICSEARCH_PORT', 9200)
    elasticsearch = ElasticsearchConnection(app.config['ELASTICSEARCH_URI'], app.config['ELASTICSEARCH_PORT'])
    elasticsearch.init_app(app)
