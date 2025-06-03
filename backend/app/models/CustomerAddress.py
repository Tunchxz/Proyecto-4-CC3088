from sqlalchemy import Column, ForeignKey, Integer
from db import Base
from sqlalchemy.orm import relationship

class CustomerAddress(Base):
    __tablename__ = 'customer_address'
    customer_id = Column(Integer, ForeignKey("customer.id"), primary_key=True)
    address_id = Column(Integer, ForeignKey("address.id"), primary_key=True)

    customer = relationship("Customer", back_populates="addresses")
    address = relationship("Address", back_populates="customer_links")