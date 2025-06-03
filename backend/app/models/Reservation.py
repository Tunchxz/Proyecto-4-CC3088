from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer
from .base import Base
from sqlalchemy.orm import relationship

class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), nullable=False)
    reservation_date = Column(Date, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status_id = Column(Integer, ForeignKey("operationstatus.id"), nullable=False)

    __table_args__ = (CheckConstraint('end_date >= start_date'),)

    customer = relationship("Customer", back_populates="reservations")