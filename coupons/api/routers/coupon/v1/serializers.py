from datetime import datetime


from datetime import date
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field, validator

from utils import validate


class CreateCouponRequest(BaseModel):
    code: str = Field(
        ...,
        title="Coupon name ex.: CARNA150",
        description="This is a coupon name, if the tourist will be use",
        max_length=8,
    )
    expiration: date = Field(
        ...,
        title="Coupon expiration date ex.: 2015-05-18",
        description="This is the coupon expiration for promotion"
    )
    discount_type: Literal['percent', 'value']
    quantity: str = Field(
        ...,
        title="Quantity the coupons make",
        description="This is the quantity the coupons will be available",
        max_length=4,
    )
    plataform: Literal['all', 'ally', 'orb', 'xpert']


class CreateCouponResponse(BaseModel):
    id: UUID
    code: str
    expire: date
    discount_type: Literal['percent', 'value']
    quantity: str
    plataform: Literal['all', 'ally', 'orb', 'xpert']
    company_id: UUID
    activated: bool