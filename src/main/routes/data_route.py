
from flask import Blueprint, current_app, jsonify, request, g, session
from src.main.adapter import flask_adapter
from src.main.factory.load_weather_controller_factory import load_weather_controller_factory
from src.main.routes.login_route import token_required

bp = Blueprint('data_route', __name__)

@bp.route('/data', methods=['POST'])
@token_required
def weather_data():
    es_logger = current_app.extensions.get('elasticsearch_logger')
    load_weather_controller = load_weather_controller_factory()
    response = flask_adapter(request=request,api_controller=load_weather_controller)
    body, status = response
    
    if status <= 299:
        cep = body['message']['cep']
        cidade = body['message']['localidade']
        user_id = session.get('user_id')
        es_logger.info(f'usuário id: {user_id} buscou o cep: {cep} correspondente a cidade {cidade}')
    
    elif status <= 499:
        error = body['error']
        es_logger.error(f'alguem tentou se cadastrar e ocorreu o seguinte erro: {error}')
    
    else:
        error = body['error']
        es_logger.critical(f'erro no servidor: {error}')
    
    return jsonify(body), status
