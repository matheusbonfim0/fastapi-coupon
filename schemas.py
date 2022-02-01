from datetime import date
from pydantic import BaseModel

class UserCreateGift(BaseModel):
    name: str
    expire: date
    percent: int
    quantity: int

class StandardOutput(BaseModel):
    message: str