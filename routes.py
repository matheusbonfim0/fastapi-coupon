from fastapi import HTTPException, APIRouter

from domain.coupon.entities import  Coupon
from domain.coupon.protocols import CouponRepo

user_router = APIRouter(prefix='/user')

@user_router.post('/create_gift')
async def create_gift(user_input: Coupon):
    try:
        await CouponRepo.create_gift(
            name=user_input.name,
            expire=user_input.expire,
            percent=user_input.percent,
            quantity=user_input.quantity
            )
        return {"message":'Cupom criado com sucesso!'}
    except Exception as error:
        raise HTTPException(400, detail=str(error))