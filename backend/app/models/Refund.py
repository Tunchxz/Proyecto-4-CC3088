from sqlalchemy import DECIMAL, CheckConstraint, Column, Date, ForeignKey, Integer, Text
from .base import Base

class Refund(Base):
    __tablename__ = 'refund'
    id = Column(Integer, primary_key=True)
    payment_id = Column(Integer, ForeignKey("payment.id"), nullable=False)
    refund_date = Column(Date, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    reason = Column(Text, nullable=False)
    status_id = Column(Integer, ForeignKey("operationstatus.id"), nullable=False)

    __table_args__ = (CheckConstraint('amount >= 0'),)