from datetime import date
from uuid import UUID

from coupons.domain.coupon.entities import Coupon
from coupons.domain.coupon.protocols import CouponRepo

from coupons.infra.database.models.coupon import Coupon as Model
from coupons.infra.database.sqlalchemy import database

class CouponRepoSQLAlchemy(CouponRepo):
    async def save(
        self,
        company_id: UUID,
        code: str, 
        expiration: date, 
        value: str,
        discount_type:str, 
        quantity: str,
        plataform: str,
    ) -> Coupon:
        values = {
            "company_id": company_id,
            "code": code,
            "expiration": expiration,
            "value": value,
            "discount_type": discount_type,
            "quantity": quantity,
            "plataform": plataform,
        }
        query = Model.insert().values(**values)

        record_id = await database.execute(query)
        return Coupon.parse_obj({"id": record_id, **values})