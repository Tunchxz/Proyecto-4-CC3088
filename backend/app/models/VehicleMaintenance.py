from sqlalchemy import Column, ForeignKey, Integer
from .base import Base

class VehicleMaintenance(Base):
    __tablename__ = 'vehicle_maintenance'
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"), primary_key=True)
    maintenance_id = Column(Integer, ForeignKey("maintenance.id"), primary_key=True)