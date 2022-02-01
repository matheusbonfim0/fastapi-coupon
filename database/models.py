from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class GiftCardDiscount(Base):
    __tablename__ = 'gift_card'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    expire = Column(Date)
    percent = Column(Integer)
    quantity = Column(Integer)

