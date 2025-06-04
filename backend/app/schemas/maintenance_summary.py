from pydantic import BaseModel
from datetime import date

class MaintenanceSummaryRead(BaseModel):
    car_plate: str
    maintenance_date: date
    description: str
    cost: float
