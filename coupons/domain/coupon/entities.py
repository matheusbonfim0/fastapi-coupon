from datetime import date
from enum import Enum

from pydantic import UUID4, BaseModel


class CouponDiscountType(str, Enum):
    percent = 'percent'
    cash_value = 'value'

class CouponPlataformUse(str, Enum):
    all_ = 'all'
    ally = 'ally'
    orb = 'orb'
    xpert = 'xpert'

class Coupon(BaseModel):
    id: UUID4
    code: str
    expiration: date
    discount_type: CouponDiscountType
    value: float
    quantity: str
    plataform: CouponPlataformUse
    company_id: UUID4
    activated: bool
