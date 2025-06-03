from sqlalchemy import Column, Date, Integer, String
from db import Base
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    driver_license_number = Column(String(64), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    phone_number = Column(String(16), nullable=False)
    registration_date = Column(Date, nullable=False)

    addresses = relationship("CustomerAddress", back_populates="customer")
    reservations = relationship("Reservation", back_populates="customer")