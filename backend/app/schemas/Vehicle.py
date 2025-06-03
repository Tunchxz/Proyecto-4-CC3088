from pydantic import BaseModel
from typing import Optional

class VehicleBase(BaseModel):
    model_id: int
    facility_id: int
    car_plate: str
    mileage: int
    status_id: int
    rates_id: int

class VehicleCreate(VehicleBase):
    pass

class VehicleRead(VehicleBase):
    id: int

    class Config:
        orm_mode = True

class VehicleUpdate(BaseModel):
    mileage: Optional[int] = None
    status_id: Optional[int] = None
    facility_id: Optional[int] = None
    