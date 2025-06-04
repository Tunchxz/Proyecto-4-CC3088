from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date
from db import get_db
from services.utils_service import calculate_rental_days, estimate_reservation_cost

router = APIRouter(prefix="/utils", tags=["Utilities"])

@router.get("/rental-days", summary="Calcular cantidad de días de renta")
def get_rental_days(
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_db)
):
    return {
        "start_date": start_date,
        "end_date": end_date,
        "rental_days": calculate_rental_days(db, start_date, end_date)
    }

@router.get("/estimate-cost/", summary="Calcular costo estimado de reserva")
def estimate_cost(
    vehicle_id: int = Query(...),
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_db)
):
    try:
        return {
            "vehicle_id": vehicle_id,
            "start_date": start_date,
            "end_date": end_date,
            "estimated_cost": estimate_reservation_cost(db, vehicle_id, start_date, end_date)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
