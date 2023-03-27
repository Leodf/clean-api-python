from flask import Flask
from flask_cors import CORS
from src.main.routes import data_route, login_route, logs_route
from . import elastic_search_logger 
from . import db
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    
    app = Flask(__name__)
    CORS(app)
    db.init_app(app)
    elastic_search_logger.init_app(app)
    
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
    app.register_blueprint(logs_route.bp, url_prefix='/api')
    
    @app.route('/', methods=['GET'])
    def home():
        return 'Api feita para a Target Data'
    
    return app


