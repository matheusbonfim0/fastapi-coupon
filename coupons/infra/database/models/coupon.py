from sqlalchemy import TIMESTAMP, UniqueConstraint, null, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import Column, Table
from sqlalchemy.sql import func
from sqlalchemy.types import Date, Text, Boolean

from coupons.infra.database.sqlalchemy import metadata

Coupon = Table(
    "coupons",
    metadata,
    Column("id", UUID(), primary_key=True, server_default=text("uuid_generate_v4()")),
    Column("code", Text(), nullable=False),
    Column("expire_at", Date(), nullable=False),
    Column("discount_type", Text(), nullable=False),
    Column("value", Text(), nullable=False),
    Column("quantity", Text(), nullable=False),
    Column("plataform", Text(), nullable=False),
    Column("company_id", UUID(), nullable=False),
    Column("activated", Boolean(), nullable=False),
    Column("created_at", TIMESTAMP, server_default=func.now()),
    Column(
        "updated_at",
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    ),
    
    UniqueConstraint('code', 'company_id'),
)
