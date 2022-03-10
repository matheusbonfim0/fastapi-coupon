
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from coupons import use_cases
from coupons.api.container import get_dependencies
from coupons.api.dependencies import get_current_user
from coupons.domain.accounts.entities import User
from coupons.domain.coupon.exceptions import CouponAlreadyRegisteredError

from .serializers import (
    CreateCouponRequest, 
    CreateCouponResponse,
    CouponAlreadyRegisteredResponse,
    )

router = APIRouter()
router = APIRouter(default_response_class=JSONResponse)
repo = get_dependencies().coupon_repo


@router.post(
    "/coupons",
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
    current_user: User = Depends(get_current_user)
):
    try: 
        coupon = await use_cases.create_coupon(
           current_user.company_id, **coupon_request.dict()
        )
        return coupon
    except CouponAlreadyRegisteredError as error:
        raise HTTPException(409, detail=error.as_dict())

