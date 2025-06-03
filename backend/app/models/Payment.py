import enum
from sqlalchemy import DECIMAL, CheckConstraint, Column, Date, Enum, ForeignKey, Integer
from db import Base

class PaymentMethodEnum(enum.Enum):
    card = 'Card'
    cash = 'Cash'
    transfer = 'Transfer'

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    rental_contract_id = Column(Integer, ForeignKey("rentalcontract.id"))
    fine_id = Column(Integer, ForeignKey("fine.id"))
    payment_date = Column(Date, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(Enum(PaymentMethodEnum), nullable=False)
    status_id = Column(Integer, ForeignKey("operationstatus.id"), nullable=False)

    __table_args__ = (CheckConstraint('amount >= 0'),)