import os
from pymongo import MongoClient
from flask import current_app

class MongoDBConnection:
    def __init__(self, uri):
        self._uri = uri
        self._client = None
        self._db = None

    def init_app(self, app):
        if not hasattr(app, "extensions"):
            app.extensions = {}

        app.extensions['mongodb'] = self

    def open_connection(self):
        self._client = MongoClient(self._uri)
        self._db = self._client[current_app.config['MONGO_DBNAME']]

    def get_connection(self):
        if self._client is None:
            self.open_connection()
        return self._client

    def get_db(self):
        if self._db is None:
            self.open_connection()
        return self._db

    def close_connection(self):
        if self._client:
            self._client.close()

def init_app(app):
    mongo_url = os.environ.get('MONGO_URL') or 'mongodb://localhost:27017'
    app.config.setdefault('MONGO_URI', mongo_url)
    app.config.setdefault('MONGO_DBNAME', 'target_api')
    mongodb = MongoDBConnection(app.config['MONGO_URI'])
    mongodb.init_app(app)