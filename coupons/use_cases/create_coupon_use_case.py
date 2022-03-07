

from datetime import date
from uuid import UUID

from coupons.domain.coupon.entities import  Coupon, CouponDiscountType, CouponPlataformUse
from coupons.domain.coupon.protocols import CouponRepo
from coupons.domain.coupon.exceptions import CouponAlreadyRegisteredError

class CreateCouponUseCase:
    def __init__(self, repo: CouponRepo) -> None:
        self._repo = repo

    async def __call__(
       self, 
       company_id: UUID,
       code: str,
       expiration: date,
       discount_type: CouponDiscountType,
       value: str,
       quantity: str,
       plataform: CouponPlataformUse,
       activated: bool = True,
    ) -> Coupon:
        coupon = await self._repo.fetch_by_company_and_coupon(
            company_id, code
        )
        if coupon:
            raise CouponAlreadyRegisteredError(code)
        coupon = await self._repo.save(
            company_id,
            code,
            expiration,
            discount_type,
            value,
            quantity,
            plataform,
            activated,
        )
        return coupon