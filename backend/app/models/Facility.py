from sqlalchemy import Column, ForeignKey, Integer, String
from db import Base
from sqlalchemy.orm import relationship

class Facility(Base):
    __tablename__ = 'facility'
    id = Column(Integer, primary_key=True)
    facility_name = Column(String(128), unique=True, nullable=False)
    facility_phone_number = Column(String(16), unique=True, nullable=False)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=False)

    address = relationship("Address", back_populates="facilities")