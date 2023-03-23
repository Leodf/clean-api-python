from bson import ObjectId
from flask import current_app
from src.data.protocols.db.add_account_repository import AddAccountRepository
from src.data.protocols.db.check_account_by_email_repository import CheckAccountByEmailRepository
from src.data.protocols.db.load_account_by_email_repository import LoadAccountByEmailRepository
from src.data.protocols.db.load_account_by_token_repository import LoadAccountByTokenRepository
from src.data.protocols.db.update_access_token_repository import UpdateAccessTokenRepository

class AccountMongoRepository(AddAccountRepository, CheckAccountByEmailRepository, LoadAccountByEmailRepository, UpdateAccessTokenRepository, LoadAccountByTokenRepository):
    
    def __init__(self):
        self.db = current_app.extensions['mongodb'].get_db()
    
    def sign_up(self, name: str, email: str, password: str) -> bool:
        accounts = self.db['accounts']
        account = accounts.insert_one({"name": name, "email": email, "password": password}).inserted_id
        
        if account:
            return True
        return False

    def check_by_email(self, email: str) -> bool:
        accounts = self.db['accounts']
        account = accounts.find_one({"email": email})
        if account:
            return True
        return False
    
    def load_by_email(self, email: str) -> dict:
        accounts = self.db['accounts']
        accountData = accounts.find_one({"email": email})
        if not accountData:
            return None
        account = {
            "id": str(accountData['_id']),
            "name": accountData['name'],
            "email": accountData['email'],
            "password": accountData['password']
        }
        
        return account
    
    def load_by_token(self, access_token: str) -> str:
        accounts = self.db['accounts']
        accountData = accounts.find_one({"access_token": access_token})
        if not accountData:
            return None
        id = str(accountData['_id'])
        return id
    
    def update_access_token(self, id: str, token: str) -> None:
        accounts = self.db['accounts']
        accounts.update_one({'_id': ObjectId(id)}, {"$set": {'access_token': token}})