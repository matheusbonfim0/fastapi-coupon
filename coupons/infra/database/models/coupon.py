from sqlalchemy import Integer, Numeric, TIMESTAMP, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import Column, Table
from sqlalchemy.sql import func
from sqlalchemy.types import Date, Text, Boolean

from coupons.infra.database.sqlalchemy import metadata

Coupon = Table(
    "coupons",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("code", Text(), nullable=False),
    Column("expire_at", Date(), nullable=False),
    Column("discount_type", Text(), nullable=False),
    Column("value", Numeric(12, 2), nullable=False),
    Column("quantity", Integer(), nullable=False),
    Column("plataform", Text(), nullable=False),
    Column("company_id", UUID(as_uuid=True), nullable=False),
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
