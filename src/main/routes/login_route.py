
from functools import wraps
from flask import Blueprint, jsonify, request, g, session, current_app

from src.main.adapter import flask_adapter
from src.main.factory.login_controller_factory import login_controller_factory
from src.main.factory.middleware_controller_factory import middleware_controller_factory
from src.main.factory.signup_controller_factory import signup_controller_factory

bp = Blueprint('login_route', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        response = flask_adapter(request=request, api_controller=middleware_controller_factory())
        
        body, status = response
        
        if status == 200:
            
            return f(*args, **kwargs)
        else:
            return jsonify(body), status

    return decorated

@bp.route('/signup', methods=['POST'])
def signup():
    session.clear()
    es_logger = current_app.extensions.get('elasticsearch_logger')
    signup_controller = signup_controller_factory()
    response = flask_adapter(request=request,api_controller=signup_controller)
    body, status = response
    
    if status <= 299:
        id = body['message']['id']
        session['user_id'] = id
        es_logger.info(f'usuário id {id} logou no sistema')
    
    elif status <= 499:
        error = body['error']
        es_logger.error(f'alguem tentou se cadastrar e ocorreu o seguinte erro: {error}')
    
    else:
        error = body['error']
        es_logger.critical(f'erro no servidor: {error}')

    return jsonify(body), status

@bp.route('/login', methods=['POST'])
def login():
    session.clear()
    es_logger = current_app.extensions.get('elasticsearch_logger')
    login_controller = login_controller_factory()
    response = flask_adapter(request=request,api_controller=login_controller)
    body, status = response
    
    if status <= 299:
        id = body['message']['id']
        session['user_id'] = id
        es_logger.info(f'usuário id {id} logou no sistema')
    
    elif status <= 499:
        error = body['error']
        es_logger.error(f'alguem tentou logar e ocorreu o seguinte erro: {error}')
    
    else:
        error = body['error']
        es_logger.critical(f'erro no servidor: {error}')

    return jsonify(body), status
    