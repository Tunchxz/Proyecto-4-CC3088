from sqlalchemy.orm import Session
from models.Reservation import Reservation
from schemas.Reservation import ReservationCreate, ReservationUpdate
from typing import List, Optional

def get_reservation(db: Session, reservation_id: int) -> Optional[Reservation]:
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def get_all_reservations(db: Session, skip: int = 0, limit: int = 100) -> List[Reservation]:
    return db.query(Reservation).offset(skip).limit(limit).all()

def create_reservation(db: Session, reservation_data: ReservationCreate) -> Reservation:
    new_reservation = Reservation(**reservation_data.model_dump())
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation

def update_reservation(db: Session, reservation_id: int, reservation_data: ReservationUpdate) -> Optional[Reservation]:
    reservation = get_reservation(db, reservation_id)
    if reservation is None:
        return None
    for key, value in reservation_data.model_dump(exclude_unset=True).items():
        setattr(reservation, key, value)
    db.commit()
    db.refresh(reservation)
    return reservation

def delete_reservation(db: Session, reservation_id: int) -> bool:
    reservation = get_reservation(db, reservation_id)
    if reservation is None:
        return False
    db.delete(reservation)
    db.commit()
    return True
