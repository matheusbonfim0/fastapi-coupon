
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
#from domain.accounts.entities import User
from domain.coupon.exceptions import CouponAlreadyRegisteredError

import use_cases
from .serializers import (
    CreateCouponRequest, 
    CreateCouponResponse,
    CouponAlreadyRegisteredResponse,
    )

router = APIRouter()
router = APIRouter(default_response_class=JSONResponse)

@router.post(
    '/coupons',
    response_model=CreateCouponResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Coupons"],
    responses={
        201: {
            "description": "Coupon created successfully", 
            "model": CreateCouponResponse
        },
        409: {
            "decription": "Coupon already registered",
            "model": CouponAlreadyRegisteredResponse,
        },
    },
)
async def create_coupon(
    coupon_request: CreateCouponRequest,
    #current_user: User
):
    try: 
        coupon = await use_cases.create_coupon(
           #current_user.company_id, 
           **coupon_request.dict()
        )
        return coupon
    except CouponAlreadyRegisteredError as error:
        raise HTTPException(409, detail=error.as_dict())

