from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Optional
from datetime import date

def get_reservation_summary(
    db: Session,
    from_date: Optional[date] = None,
    to_date: Optional[date] = None,
    status: Optional[str] = None,
    customer_name: Optional[str] = None,
    car_plate: Optional[str] = None
) -> List[dict]:
    """
    Obtiene un resumen de reservaciones con filtros opcionales.
    
    Args:
        db: Sesión de base de datos
        from_date: Fecha de inicio del filtro (opcional)
        to_date: Fecha de fin del filtro (opcional)
        status: Estado de la reservación para filtrar (opcional)
        customer_name: Nombre del cliente para filtrar (opcional)
        car_plate: Placa del vehículo para filtrar (opcional)
    
    Returns:
        Lista de diccionarios con los datos de las reservaciones
    """
    sql = """
        SELECT *
        FROM view_reservation_summary
        WHERE
            (:from_date IS NULL OR start_date >= :from_date)
            AND (:to_date IS NULL OR end_date <= :to_date)
            AND (:status IS NULL OR reservation_status ILIKE :status)
            AND (:customer_name IS NULL OR customer_name ILIKE :customer_name_pattern)
            AND (:car_plate IS NULL OR car_plate ILIKE :car_plate_pattern)
        ORDER BY start_date DESC
    """
    
    result = db.execute(text(sql), {
        "from_date": from_date,
        "to_date": to_date,
        "status": status,
        "customer_name": customer_name,
        "customer_name_pattern": f"%{customer_name}%" if customer_name else None,
        "car_plate": car_plate,
        "car_plate_pattern": f"%{car_plate}%" if car_plate else None
    })
    
    # Usar _mapping para compatibilidad con versiones recientes de SQLAlchemy
    return [dict(row._mapping) for row in result.fetchall()]

def get_maintenance_summary(
    db: Session,
    car_plate: Optional[str] = None,
    min_cost: Optional[float] = None,
    max_cost: Optional[float] = None,
    from_date: Optional[date] = None,
    to_date: Optional[date] = None
) -> List[dict]:
    """
    Obtiene un resumen del historial de mantenimiento con filtros opcionales.
    
    Args:
        db: Sesión de base de datos
        car_plate: Placa del vehículo para filtrar (búsqueda parcial, opcional)
        min_cost: Costo mínimo del mantenimiento (opcional)
        max_cost: Costo máximo del mantenimiento (opcional)
        from_date: Fecha de inicio del filtro (opcional)
        to_date: Fecha de fin del filtro (opcional)
    
    Returns:
        Lista de diccionarios con los datos del historial de mantenimiento
    """
    sql = """
        SELECT *
        FROM view_vehicle_maintenance_history
        WHERE
            CASE WHEN :car_plate IS NOT NULL THEN car_plate ILIKE CONCAT('%', :car_plate, '%') ELSE TRUE END
            AND CASE WHEN :min_cost IS NOT NULL THEN cost >= :min_cost ELSE TRUE END
            AND CASE WHEN :max_cost IS NOT NULL THEN cost <= :max_cost ELSE TRUE END
            AND CASE WHEN :from_date IS NOT NULL THEN maintenance_date >= :from_date ELSE TRUE END
            AND CASE WHEN :to_date IS NOT NULL THEN maintenance_date <= :to_date ELSE TRUE END
        ORDER BY maintenance_date DESC
    """
    
    result = db.execute(text(sql), {
        "car_plate": car_plate,
        "min_cost": min_cost,
        "max_cost": max_cost,
        "from_date": from_date,
        "to_date": to_date
    })
    
    # Usar _mapping para compatibilidad con versiones recientes de SQLAlchemy
    return [dict(row._mapping) for row in result.fetchall()]

def get_contract_income_summary(
    db: Session,
    contract_id: Optional[int] = None,
    min_total_income: Optional[float] = None,
    max_total_income: Optional[float] = None,
    min_fines: Optional[float] = None,
    max_fines: Optional[float] = None
) -> List[dict]:
    """
    Obtiene un resumen de ingresos por contrato con filtros opcionales.
    
    Args:
        db: Sesión de base de datos
        contract_id: ID específico del contrato a filtrar (opcional)
        min_total_income: Ingreso total mínimo (opcional)
        max_total_income: Ingreso total máximo (opcional)
        min_fines: Multas mínimas (opcional)
        max_fines: Multas máximas (opcional)
    
    Returns:
        Lista de diccionarios con los datos de ingresos por contrato
    """
    sql = """
        SELECT *
        FROM view_total_income_per_contract
        WHERE
            CASE WHEN :contract_id IS NOT NULL THEN contract_id = :contract_id ELSE TRUE END
            AND CASE WHEN :min_total_income IS NOT NULL THEN total_income >= :min_total_income ELSE TRUE END
            AND CASE WHEN :max_total_income IS NOT NULL THEN total_income <= :max_total_income ELSE TRUE END
            AND CASE WHEN :min_fines IS NOT NULL THEN total_fines >= :min_fines ELSE TRUE END
            AND CASE WHEN :max_fines IS NOT NULL THEN total_fines <= :max_fines ELSE TRUE END
        ORDER BY total_income DESC
    """
    
    result = db.execute(text(sql), {
        "contract_id": contract_id,
        "min_total_income": min_total_income,
        "max_total_income": max_total_income,
        "min_fines": min_fines,
        "max_fines": max_fines
    })
    
    # Usar _mapping para compatibilidad con versiones recientes de SQLAlchemy
    return [dict(row._mapping) for row in result.fetchall()]
