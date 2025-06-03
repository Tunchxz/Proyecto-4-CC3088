from sqlalchemy import Column, ForeignKey, Integer, String
from .base import Base
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    unit_number = Column(String(8))
    street_number = Column(String(8))
    address_line_1 = Column(String(64), nullable=False)
    address_line_2 = Column(String(64))
    city = Column(String(64), nullable=False)
    region = Column(String(64))
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)

    country = relationship("Country", back_populates="addresses")
    facilities = relationship("Facility", back_populates="address")
    customer_links = relationship("CustomerAddress", back_populates="address")