
from flask import Blueprint, jsonify, request, g, session
from src.main.adapter import flask_adapter
from src.main.factory.load_weather_controller_factory import load_weather_controller_factory
from src.main.factory.log_controller_factory import log_controller_factory
from src.main.routes.login_route import token_required

bp = Blueprint('data_route', __name__)

@bp.route('/data', methods=['POST'])
@token_required
def weather_data():
    load_weather_controller = log_controller_factory(load_weather_controller_factory())
    response = flask_adapter(request=request,api_controller=load_weather_controller)
    message, status = response
    
    return jsonify(message), status
