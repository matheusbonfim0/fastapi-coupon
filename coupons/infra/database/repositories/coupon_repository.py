from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from coupons.domain.coupon.entities import Coupon
from coupons.domain.coupon.protocols import CouponRepo
from coupons.infra.database.models.coupon import Coupon as Model
from coupons.infra.database.sqlalchemy import database


def _to_entity(record) -> Coupon:
    values = dict(record)
    values['expiration'] = values.pop('expire_at')
    return Coupon.model_validate(values)


class CouponRepoSQLAlchemy(CouponRepo):
    async def fetch_by_company_and_coupon(
        self, company_id: UUID, code: str
    ) -> Optional[Coupon]:
        query = Model.select().where(
            Model.c.company_id == company_id,
            Model.c.code == code,
        )
        record = await database.fetch_one(query)
        return _to_entity(record) if record else None

    async def save(
        self,
        company_id: UUID,
        code: str,
        expiration: date,
        value: float,
        discount_type: str,
        quantity: int,
        plataform: str,
        activated: bool,
    ) -> Coupon:
        values = {
            'id': uuid4(),
            'company_id': company_id,
            'code': code,
            'expire_at': expiration,
            'value': value,
            'discount_type': discount_type,
            'quantity': quantity,
            'plataform': plataform,
            'activated': activated,
        }
        await database.execute(Model.insert().values(**values))
        return _to_entity(values)
