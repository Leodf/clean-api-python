
from flask import Blueprint, jsonify, request
from src.main.adapter import flask_adapter
from src.main.factory.log_controller_factory import log_controller_factory
from src.main.routes.login_route import token_required

bp = Blueprint('logs_route', __name__)

@bp.route('/logs', methods=['GET'])
@token_required
def logs():
    log_controller = log_controller_factory()
    response = flask_adapter(request=request,api_controller=log_controller)
    body, status = response

    return jsonify(body), status
