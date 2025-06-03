from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas.Vehicle import VehicleCreate, VehicleRead, VehicleUpdate
from services.vehicle_service import (
    get_vehicle, get_all_vehicles, create_vehicle, update_vehicle, delete_vehicle
)
from db import get_db

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.get("/", response_model=List[VehicleRead])
def list_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_vehicles(db, skip, limit)

@router.get("/{vehicle_id}", response_model=VehicleRead)
def retrieve_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = get_vehicle(db, vehicle_id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.post("/", response_model=VehicleRead, status_code=status.HTTP_201_CREATED)
def create_new_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db, vehicle)

@router.put("/{vehicle_id}", response_model=VehicleRead)
def update_existing_vehicle(vehicle_id: int, update_data: VehicleUpdate, db: Session = Depends(get_db)):
    vehicle = update_vehicle(db, vehicle_id, update_data)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    success = delete_vehicle(db, vehicle_id)
    if not success:
        raise HTTPException(status_code=404, detail="Vehicle not found")
