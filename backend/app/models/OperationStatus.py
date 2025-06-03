from sqlalchemy import Column, Integer, String
from .base import Base

class OperationStatus(Base):
    __tablename__ = 'operationstatus'
    id = Column(Integer, primary_key=True)
    status_name = Column(String(64), unique=True, nullable=False)