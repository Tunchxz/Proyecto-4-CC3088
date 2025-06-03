from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String
from .base import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("model.id"), nullable=False)
    facility_id = Column(Integer, ForeignKey("facility.id"), nullable=False)
    car_plate = Column(String(64), unique=True, nullable=False)
    mileage = Column(Integer, nullable=False)
    status_id = Column(Integer, ForeignKey("operationstatus.id"), nullable=False)
    rates_id = Column(Integer, ForeignKey("rates.id"), nullable=False)

    __table_args__ = (CheckConstraint('mileage >= 0'),)