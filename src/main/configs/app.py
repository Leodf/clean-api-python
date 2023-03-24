from flask import Flask
from flask_cors import CORS
from src.main.routes import data_route, login_route
from . import db
from . import elasticsearch
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    
    app = Flask(__name__)
    CORS(app)
    db.init_app(app)
    elasticsearch.init_app(app)
    
    app.config['SECRET_KEY'] = 'secret'
    SWAGGER_URL = '/docs'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'target-api': 'api para busca da previsão do tempo'
        }
    )
    
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)
    app.register_blueprint(login_route.bp, url_prefix='/api')
    app.register_blueprint(data_route.bp, url_prefix='/api')
    
    @app.route('/', methods=['GET'])
    def home():
        return 'Hello World!'
    
    return app


