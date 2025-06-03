from sqlalchemy import Column, Integer, String
from .base import Base

class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    manufacturer_name = Column(String(128), unique=True, nullable=False)