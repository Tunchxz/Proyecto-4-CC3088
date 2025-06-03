from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentLogRead(BaseModel):
    id: int
    payment_id: Optional[int]
    log_date: datetime
    amount: float
    method: str

    class Config:
        orm_mode = True
