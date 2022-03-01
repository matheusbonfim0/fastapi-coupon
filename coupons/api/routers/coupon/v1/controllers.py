from http import HTTPStatus
from http.client import responses

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import use_cases

from use_cases.create_coupon_use_case import CreateCouponUseCase
from .serializers import CreateCouponRequest, CreateCouponResponse

router = APIRouter()
router = APIRouter(default_response_class=JSONResponse)

@router.post(
    '/coupons',
    response_model=CreateCouponResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {
            "description": "Coupon registered", 
            "model": CreateCouponResponse},
        409: {
            "decription": "Coupon already registered",
            "model": "",
        },
    },
)
async def create_coupon(
    coupon_request: CreateCouponRequest,
    
):
    try: 
        coupon = await use_cases.create_coupon(
            **coupon_request.dict()
        )
        return coupon
    except Exception as error:
        raise HTTPException(409, detail=error.as_dict())