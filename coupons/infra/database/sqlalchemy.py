from contextlib import asynccontextmanager

import databases

from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

from coupons.config.environment import get_settings

_SETTINGS = get_settings()

database = databases.Database(_SETTINGS.DATABASE_URL)
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s", 
    }
)

@asynccontextmanager
async def database_context():
    await connect_database()
    yield database
    await disconnect_database()

async def connect_database():
    await database.connect()

async def disconnect_database():
    await database.disconnect()

def init_database() -> None: 
    import coupons.infra.database.models

    metadata.bind = create_engine(_SETTINGS.DATABASE_URL)