from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

ViewBase = declarative_base()

class CustomerView(ViewBase):
    __tablename__ = 'customer_view'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    registration_date = Column(Date)


class VehicleView(ViewBase):
    __tablename__ = 'vehicle_view'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    car_plate = Column(String)
    mileage = Column(Integer)
    status_id = Column(Integer)
    model_id = Column(Integer)
    facility_id = Column(Integer)
    rates_id = Column(Integer)


class ReservationView(ViewBase):
    __tablename__ = 'reservation_view'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    vehicle_id = Column(Integer)
    reservation_date = Column(Date)
    start_date = Column(Date)
    end_date = Column(Date)
    status_id = Column(Integer)
