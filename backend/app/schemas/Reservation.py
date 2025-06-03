from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReservationBase(BaseModel):
    customer_id: int
    vehicle_id: int
    start_date: date
    end_date: date
    status_id: int

class ReservationCreate(ReservationBase):
    pass

class ReservationRead(ReservationBase):
    id: int
    reservation_date: date

    class Config:
        orm_mode = True

class ReservationUpdate(BaseModel):
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status_id: Optional[int] = None
