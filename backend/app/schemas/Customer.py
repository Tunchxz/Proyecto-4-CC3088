from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    driver_license_number: str
    email: EmailStr
    phone_number: str

class CustomerCreate(CustomerBase):
    pass

class CustomerRead(CustomerBase):
    id: int
    registration_date: date

    class Config:
        orm_mode = True

class CustomerUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    