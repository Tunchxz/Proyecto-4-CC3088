from sqlalchemy import DECIMAL, CheckConstraint, Column, Date, Integer, Text
from db import Base

class Maintenance(Base):
    __tablename__ = 'maintenance'
    id = Column(Integer, primary_key=True)
    maintenance_date = Column(Date, nullable=False)
    description = Column(Text, nullable=False)
    cost = Column(DECIMAL(10, 2), nullable=False)

    __table_args__ = (CheckConstraint('cost >= 0'),)