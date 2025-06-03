from sqlalchemy import Column, Integer, String
from .base import Base

class VehicleType(Base):
    __tablename__ = 'vehicletype'
    id = Column(Integer, primary_key=True)
    vehicle_type_name = Column(String(32), unique=True, nullable=False)