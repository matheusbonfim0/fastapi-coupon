from datetime import date
from typing import Optional, Protocol
from uuid import UUID
from .entities import Coupon

class CouponRepo(Protocol):
    async def fetch_by_company_and_coupon(
        self, company_id: UUID, code: str
    ) -> Optional[Coupon]:
        ...

    async def save(
        self,
        company_id: UUID,
        code: str, 
        expiration: date, 
        value: float,
        discount_type: str,
        quantity: int,
        plataform: str,
        activated: bool,
    ) -> Coupon:
        ...
