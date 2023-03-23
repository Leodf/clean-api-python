

from src.data.protocols.criptography.encrypter import Encrypter
from src.data.protocols.criptography.hash_comparer import HashComparer
from src.data.protocols.db.load_account_by_email_repository import LoadAccountByEmailRepository
from src.data.protocols.db.update_access_token_repository import UpdateAccessTokenRepository
from src.domain.entity.auth import AuthEntity
from src.domain.usecase.authentication import Authentication


class DbAuthentication(Authentication):
    def __init__(
        self,
        load_account_by_email_repository: LoadAccountByEmailRepository,
        hash_comparer: HashComparer,
        encrypter: Encrypter,
        update_access_token_repository: UpdateAccessTokenRepository
    ):
        self.load_account_by_email_repository = load_account_by_email_repository
        self.hash_comparer = hash_comparer
        self.encrypter = encrypter
        self.update_access_token_repository = update_access_token_repository
    
    def auth(self, email: str, password: str) -> AuthEntity:
        account = self.load_account_by_email_repository.load_by_email(email)
        if account:
            is_valid = self.hash_comparer.compare(account['password'], password)
            if is_valid:
                access_token = self.encrypter.encrypt(account['id'])
                self.update_access_token_repository.update_access_token(account['id'], access_token)
                authentication = AuthEntity(access_token, account['name'])
                return authentication.toJson()
            
        return None