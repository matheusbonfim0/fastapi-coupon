

from datetime import date
from uuid import UUID

from domain.coupon.entities import  Coupon, CouponDiscountType, CouponPlataformUse
from domain.coupon.protocols import CouponRepo


class CreateCouponUseCase:
    def __init__(self, repo: CouponRepo) -> None:
        self._repo = repo

    async def __call__(
       self, 
       company_id: UUID,
       name: str,
       expiration: date,
       discount_type: CouponDiscountType,
       quantity: str,
       plataform: CouponPlataformUse,
       activated: bool,
    ) -> Coupon:
        ...