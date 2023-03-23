from flask import current_app
from src.data.usecase.db_authentication import DbAuthentication
from src.infra.criptography.pyjwt_adapter import PyJwtAdapter
from src.infra.criptography.werkzeug_adapter import WerkzeugAdapter
from src.infra.db.account_mongo_repository import AccountMongoRepository
from src.presentation.controllers.login_controller import LoginController
from src.presentation.protocols.controller import Controller

def login_controller_factory() -> Controller:
    
    werkzeug_hasher = WerkzeugAdapter(12)
    jwt_encrypter = PyJwtAdapter(current_app.config['SECRET_KEY'])
    account_repository = AccountMongoRepository()
    db_authentication = DbAuthentication(account_repository, werkzeug_hasher, jwt_encrypter, account_repository)
    login_controller_factory = LoginController(db_authentication)
    
    return login_controller_factory