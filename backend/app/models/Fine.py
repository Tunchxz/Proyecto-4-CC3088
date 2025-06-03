from sqlalchemy import DECIMAL, CheckConstraint, Column, Date, ForeignKey, Integer, Text
from db import Base

class Fine(Base):
    __tablename__ = 'fine'
    id = Column(Integer, primary_key=True)
    rental_contract_id = Column(Integer, ForeignKey("rentalcontract.id"), nullable=False)
    fine_date = Column(Date, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    reason = Column(Text, nullable=False)
    status_id = Column(Integer, ForeignKey("operationstatus.id"), nullable=False)

    __table_args__ = (CheckConstraint('amount >= 0'),)