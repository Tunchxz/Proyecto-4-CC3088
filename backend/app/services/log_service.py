from sqlalchemy.orm import Session
from models.logs import PaymentLog
from typing import List

def get_payment_logs(db: Session, skip: int = 0, limit: int = 100) -> List[PaymentLog]:
    return db.query(PaymentLog).order_by(PaymentLog.log_date.desc()).offset(skip).limit(limit).all()
