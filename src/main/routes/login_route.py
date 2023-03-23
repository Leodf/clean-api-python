
from functools import wraps
from flask import Blueprint, jsonify, request

from src.main.adapter import flask_adapter
from src.main.factory.login_controller_factory import login_controller_factory
from src.main.factory.middleware_controller_factory import middleware_controller_factory
from src.main.factory.signup_controller_factory import signup_controller_factory

bp = Blueprint('login_route', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # print(request.headers)
        response = flask_adapter(request=request, api_controller=middleware_controller_factory())
        
        message, status = response
        
        if status == 200:
            return f(*args, **kwargs)
        else:
            return jsonify(message), status

    return decorated

@bp.route('/signup', methods=['POST'])
def signup():
    response = flask_adapter(request=request,api_controller=signup_controller_factory())
    message, status = response
    
    return jsonify(message), status

@bp.route('/login', methods=['POST'])
def login():
    response = flask_adapter(request=request,api_controller=login_controller_factory())
    message, status = response
    
    return jsonify(message), status
