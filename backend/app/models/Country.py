from sqlalchemy import Column, Integer, String
from .base import Base
from sqlalchemy.orm import relationship

class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    country_name = Column(String(64), unique=True, nullable=False)

    addresses = relationship("Address", back_populates="country")