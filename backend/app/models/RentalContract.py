from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer
from db import Base

class RentalContract(Base):
    __tablename__ = 'rentalcontract'
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey("reservation.id"), unique=True, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status_id = Column(Integer, ForeignKey("operationstatus.id"), nullable=False)

    __table_args__ = (CheckConstraint('end_date >= start_date'),)