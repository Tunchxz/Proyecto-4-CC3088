from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas.Reservation import ReservationCreate, ReservationRead, ReservationUpdate
from services.reservation_service import (
    get_reservation, get_all_reservations, create_reservation, update_reservation, delete_reservation
)
from db import get_db

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.get("/", response_model=List[ReservationRead])
def list_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_reservations(db, skip, limit)

@router.get("/{reservation_id}", response_model=ReservationRead)
def retrieve_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = get_reservation(db, reservation_id)
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.post("/", response_model=ReservationRead, status_code=status.HTTP_201_CREATED)
def create_new_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation(db, reservation)

@router.put("/{reservation_id}", response_model=ReservationRead)
def update_existing_reservation(reservation_id: int, update_data: ReservationUpdate, db: Session = Depends(get_db)):
    reservation = update_reservation(db, reservation_id, update_data)
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_reservation(reservation_id: int, db: Session = Depends(get_db)):
    success = delete_reservation(db, reservation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Reservation not found")
