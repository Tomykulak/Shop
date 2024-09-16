# db models
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)  # Inventory quantity

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float)


