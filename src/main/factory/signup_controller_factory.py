from flask import current_app
from src.data.usecase.db_add_account import DbAddAccount
from src.data.usecase.db_authentication import DbAuthentication
from src.infra.criptography.pyjwt_adapter import PyJwtAdapter
from src.infra.criptography.werkzeug_adapter import WerkzeugAdapter
from src.infra.db.account_mongo_repository import AccountMongoRepository
from src.presentation.controllers.signup_controller import SignUpController
from src.presentation.protocols.controller import Controller

def signup_controller_factory() -> Controller:
    
    werkzeug_hasher = WerkzeugAdapter(12)
    jwt_encrypter = PyJwtAdapter(current_app.config['SECRET_KEY'])
    account_repository = AccountMongoRepository()
    
    db_add_account = DbAddAccount(werkzeug_hasher, account_repository, account_repository)
    db_authentication = DbAuthentication(account_repository, werkzeug_hasher, jwt_encrypter, account_repository)
    signup_controller_factory = SignUpController(db_add_account, db_authentication)
    
    return signup_controller_factory