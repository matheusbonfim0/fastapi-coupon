

from datetime import date
from uuid import UUID

from domain.coupon.entities import  Coupon, CouponDiscountType, CouponPlataformUse
from domain.coupon.protocols import CouponRepo
from domain.coupon.exceptions import CouponAlreadyRegisteredError

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
        coupon = await self._repo.fetch_by_company_and_coupon(
            company_id, name
        )
        if coupon:
            raise CouponAlreadyRegisteredError(name)
        coupon = await self._repo.save(
            company_id,
            name,
            expiration,
            discount_type,
            quantity,
            plataform,
            activated,
        )
        return coupon