from sqlalchemy import text
from sqlalchemy.orm import Session
from datetime import date

def calculate_rental_days(db: Session, start_date: date, end_date: date) -> int:
    sql = text("SELECT calculate_rental_days(:start_date, :end_date) AS days")
    result = db.execute(sql, {
        "start_date": start_date,
        "end_date": end_date
    }).fetchone()
    return int(result.days) if result and result.days is not None else 0

def estimate_reservation_cost(
    db: Session,
    vehicle_id: int,
    start_date: date,
    end_date: date
) -> float:
    sql = text("""
        SELECT calculate_reservation_cost(:vehicle_id, :start_date, :end_date) AS cost
    """)
    result = db.execute(sql, {
        "vehicle_id": vehicle_id,
        "start_date": start_date,
        "end_date": end_date
    }).fetchone()
    return float(result.cost) if result and result.cost is not None else 0.0
