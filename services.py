from datetime import date
from database.connection import async_session
from database.models import GiftCardDiscount

class UserService:
    async def create_gift(name: str, expire: date, percent: int, quantity: int ):
        async with async_session() as session:
            session.add(GiftCardDiscount(name=name, expire=expire, percent=percent, quantity=quantity))
            await session.commit()