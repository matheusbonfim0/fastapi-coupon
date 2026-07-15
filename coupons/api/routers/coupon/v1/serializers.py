
from datetime import date
from uuid import UUID

from pydantic import UUID4, BaseModel, Field, field_validator
from coupons.domain.coupon.entities import CouponDiscountType, CouponPlataformUse

from coupons.utils import validate


class CreateCouponRequest(BaseModel):
    code: str = Field(
        ...,
        title="Coupon name ex.: CARNA150",
        description="This is a coupon name, if the tourist will be use",
        
    )
    expiration: date = Field(
        ...,
        title="Coupon expiration date ex.: 2015-05-18",
        description="This is the coupon expiration for promotion"
    )
    discount_type: CouponDiscountType
    value: float = Field(
        ...,
        title="Coupon Value",
        description="This is the value about theu coupons",
    )
    quantity: int = Field(
        ...,
        title="Quantity the coupons make",
        description="This is the quantity the coupons will be available",
        gt=0,
    )
    plataform: CouponPlataformUse

    @field_validator("expiration")
    @classmethod
    def validate_expiration(cls, expiration):
        if not validate.expiry_date_greater_than_current_date(expiration):
            raise ValueError("must be a valid date")
        return expiration

class CreateCouponResponse(BaseModel):
    id: UUID4
    code: str
    expiration: date
    discount_type: CouponDiscountType
    value: float
    quantity: int
    plataform: CouponPlataformUse
    company_id: UUID
    activated: bool

class CouponAlreadyRegisteredResponse(BaseModel):
    class Detail(BaseModel):
        msg: str
        id: str
    
    detail: Detail

class CouponNotFoundResponse(BaseModel):
    class Detail(BaseModel):
        msg: str
        id: str

    detail: Detail
