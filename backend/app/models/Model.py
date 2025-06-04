from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint
from db import Base
from sqlalchemy.orm import relationship
import enum

class TransmissionEnum(enum.Enum):
    manual = 'manual'
    automatic = 'automatic'
    continuously_variable = 'continuously variable'

class SeatsEnum(enum.Enum):
    two = 'two'
    five = 'five'
    seven = 'seven'
    eight = 'eight'
    
class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturer.id"), nullable=False)
    model_name = Column(String(128), nullable=False)
    transmission_type = Column(Enum(TransmissionEnum), nullable=False)
    capacity = Column(Enum(SeatsEnum), nullable=False)
    vehicle_type_id = Column(Integer, ForeignKey("vehicletype.id"), nullable=False)

    __table_args__ = (UniqueConstraint('manufacturer_id', 'model_name'),)

    colors = relationship("ModelColor", back_populates="model")