from sqlalchemy import Column, Integer, Numeric, String, TIMESTAMP
from db import Base

class PaymentLog(Base):
    __tablename__ = "payment_log"

    id = Column(Integer, primary_key=True)
    payment_id = Column(Integer)
    log_date = Column(TIMESTAMP)
    amount = Column(Numeric)
    method = Column(String)
