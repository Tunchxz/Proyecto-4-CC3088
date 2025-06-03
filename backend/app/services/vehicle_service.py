from sqlalchemy.orm import Session
from models.Vehicle import Vehicle
from schemas.Vehicle import VehicleCreate, VehicleUpdate
from typing import List, Optional

def get_vehicle(db: Session, vehicle_id: int) -> Optional[Vehicle]:
    return db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

def get_all_vehicles(db: Session, skip: int = 0, limit: int = 100) -> List[Vehicle]:
    return db.query(Vehicle).offset(skip).limit(limit).all()

def create_vehicle(db: Session, vehicle_data: VehicleCreate) -> Vehicle:
    new_vehicle = Vehicle(**vehicle_data.model_dump())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

def update_vehicle(db: Session, vehicle_id: int, vehicle_data: VehicleUpdate) -> Optional[Vehicle]:
    vehicle = get_vehicle(db, vehicle_id)
    if vehicle is None:
        return None
    for key, value in vehicle_data.model_dump(exclude_unset=True).items():
        setattr(vehicle, key, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def delete_vehicle(db: Session, vehicle_id: int) -> bool:
    vehicle = get_vehicle(db, vehicle_id)
    if vehicle is None:
        return False
    db.delete(vehicle)
    db.commit()
    return True
