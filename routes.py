from fastapi import HTTPException, APIRouter

from coupons.domain.coupon.entities import  Coupon
from coupons.domain.coupon.protocols import CouponRepo

user_router = APIRouter(prefix='/user')

@user_router.post('/create_gift')
async def create_gift(user_input: Coupon):
    try:
        await CouponRepo.create_gift(
            code=user_input.code,
            expire=user_input.expire,
            percent=user_input.percent,
            quantity=user_input.quantity
            )
        return {"message":'Cupom criado com sucesso!'}
    except Exception as error:
        raise HTTPException(400, detail=str(error))