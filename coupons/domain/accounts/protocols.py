from typing import Protocol

from coupons.domain.accounts.entities import User

class UserRepo(Protocol):
    def fetch_by_token(self, token: str) -> User:
        ...