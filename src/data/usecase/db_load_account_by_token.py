
from src.data.protocols.criptography.decrypter import Decrypter
from src.data.protocols.db.load_account_by_token_repository import LoadAccountByTokenRepository
from src.domain.usecase.load_account_by_token import LoadAccountByToken

class DbLoadAccountByToken(LoadAccountByToken):
    def __init__(
        self,
        decrypter: Decrypter,
        load_account_by_token_repository: LoadAccountByTokenRepository
    ):
        self.decrypter = decrypter
        self.load_account_by_token_repository = load_account_by_token_repository
    
    def load_by_token(self, access_token: str) -> str:
        token = None
        try:
            token = self.decrypter.decrypt(access_token)
        except:
            return None
        
        if token:
            account_id = self.load_account_by_token_repository.load_by_token(access_token)
            if account_id:
                return account_id
        
        return None