from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from db import get_db
from schemas.reservation_summary import ReservationSummaryRead
from schemas.maintenance_summary import MaintenanceSummaryRead
from schemas.contract_income_summary import ContractIncomeSummaryRead
from services.analytics_service import get_contract_income_summary, get_maintenance_summary, get_reservation_summary
from datetime import date

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/reservations", response_model=List[ReservationSummaryRead])
def read_reservation_summary(
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return get_reservation_summary(db, from_date, to_date, status)

@router.get("/maintenance", response_model=List[MaintenanceSummaryRead])
def read_maintenance_summary(
    car_plate: Optional[str] = Query(None, description="Filtro parcial por matrícula"),
    min_cost: Optional[float] = Query(None),
    max_cost: Optional[float] = Query(None),
    from_date: Optional[date] = Query(None),
    to_date: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    return get_maintenance_summary(db, car_plate, min_cost, max_cost, from_date, to_date)

@router.get("/contracts/income", response_model=List[ContractIncomeSummaryRead])
def read_contract_income_summary(
    contract_id: Optional[int] = Query(None),
    min_total_income: Optional[float] = Query(None),
    max_total_income: Optional[float] = Query(None),
    min_fines: Optional[float] = Query(None),
    max_fines: Optional[float] = Query(None),
    db: Session = Depends(get_db)
):
    return get_contract_income_summary(
        db, contract_id, min_total_income, max_total_income, min_fines, max_fines
    )
