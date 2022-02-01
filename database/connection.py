from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = getenv("DATABASE_URL")

engine = create_async_engine("postgresql+asyncpg://admin:admin@localhost:5432/fastapi")
async_session = sessionmaker(engine, class_=AsyncSession)