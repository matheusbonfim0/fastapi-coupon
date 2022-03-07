from datetime import date
from typing import Protocol
from uuid import UUID
from .entities import Coupon

class CouponRepo(Protocol):
    async def save(
        self,
        company_id: UUID,
        code: str, 
        expiration: date, 
        value: str,
        discount_type:str, 
        quantity: str,
        plataform: str,

    ) -> Coupon:
        ...