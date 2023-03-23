
from src.data.protocols.criptography.hasher import Hasher
from src.data.protocols.db.add_account_repository import AddAccountRepository
from src.data.protocols.db.check_account_by_email_repository import CheckAccountByEmailRepository
from src.domain.usecase.add_account import AddAccount

class DbAddAccount(AddAccount):
    
    def __init__(
        self,
        hasher: Hasher,
        add_account_repository: AddAccountRepository,
        check_account_by_email_repository: CheckAccountByEmailRepository
    ):
        self.hasher = hasher
        self.add_account_repository = add_account_repository
        self.check_account_by_email_repository = check_account_by_email_repository
    
    def sign_up(self, name: str, email: str, password: str) -> bool:
        exists = self.check_account_by_email_repository.check_by_email(email)
        is_valid = False
        if not exists:
            hashed_password = self.hasher.hash(password)
            is_valid = self.add_account_repository.sign_up(name, email, hashed_password) 
    
        return is_valid