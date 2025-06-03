from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.logs import PaymentLogRead
from services.log_service import get_payment_logs
from db import get_db

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/payments", response_model=List[PaymentLogRead])
def read_payment_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_payment_logs(db, skip, limit)
