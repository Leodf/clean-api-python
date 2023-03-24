
from functools import wraps
from flask import Blueprint, jsonify, request, g, session

from src.main.adapter import flask_adapter
from src.main.factory.log_controller_factory import log_controller_factory
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
    signup_controller = log_controller_factory(signup_controller_factory())
    response = flask_adapter(request=request,api_controller=signup_controller)
    body, status = response

    return jsonify(body), status

@bp.route('/login', methods=['POST'])
def login():
    login_controller = log_controller_factory(login_controller_factory())
    response = flask_adapter(request=request,api_controller=login_controller)
    body, status = response
    
    return jsonify(body), status