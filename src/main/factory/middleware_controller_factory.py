from flask import current_app
from src.data.usecase.db_load_account_by_token import DbLoadAccountByToken
from src.infra.criptography.pyjwt_adapter import PyJwtAdapter
from src.infra.db.account_mongo_repository import AccountMongoRepository
from src.presentation.middleware.auth_middleware import AuthMiddleware
from src.presentation.protocols.controller import Controller

def middleware_controller_factory() -> Controller:
    
    jwt_decrypter = PyJwtAdapter(current_app.config['SECRET_KEY'])
    account_repository = AccountMongoRepository()
    load_account_by_token = DbLoadAccountByToken(jwt_decrypter, account_repository)
    middleware_controller_factory = AuthMiddleware(load_account_by_token)
    
    return middleware_controller_factory