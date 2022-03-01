from enum import Enum
from typing import List
from pydantic import UUID4, BaseModel, EmailStr

class UserRole(str, Enum):
    admin = 'admin'
    tourist = 'tourist'

class User(BaseModel):
    id: UUID4
    name: str
    email: EmailStr
    company_id: UUID4
    roles: List[UserRole]