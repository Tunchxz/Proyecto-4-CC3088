from sqlalchemy import DECIMAL, CheckConstraint, Column, Integer
from db import Base

class Rates(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key=True)
    daily_rate = Column(DECIMAL(10,2), nullable=False)
    weekly_rate = Column(DECIMAL(10,2), nullable=False)
    monthly_rate = Column(DECIMAL(10,2), nullable=False)

    __table_args__ = (
        CheckConstraint('daily_rate >= 0'),
        CheckConstraint('weekly_rate >= 0'),
        CheckConstraint('monthly_rate >= 0'),
    )