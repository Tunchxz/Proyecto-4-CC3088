from pydantic import BaseModel
from datetime import date

class ReservationSummaryRead(BaseModel):
    reservation_id: int
    customer_name: str
    car_plate: str
    start_date: date
    end_date: date
    reservation_status: str
