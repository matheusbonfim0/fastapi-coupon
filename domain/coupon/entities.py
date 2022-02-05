from datetime import date
from enum import Enum

from pydantic import UUID4, BaseModel


class CouponDiscountType(str, Enum):
    percent = 'percent'
    cash_value = 'value'

class CouponPlataformUse(str, Enum):
    all_ = 'all'
    ally = 'Ally'
    orb = 'ORB'
    xpert = 'Xpert'

class Coupon(BaseModel):
    id: UUID4
    name: str
    expire: date
    discount_type: CouponDiscountType
    quantity: str
    plataform: CouponPlataformUse
    company_id: UUID4
    activated: bool
