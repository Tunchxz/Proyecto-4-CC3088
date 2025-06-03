from sqlalchemy.orm import Session
from models.Customer import Customer
from schemas.Customer import CustomerCreate, CustomerUpdate
from typing import List, Optional

def get_customer(db: Session, customer_id: int) -> Optional[Customer]:
    return db.query(Customer).filter(Customer.id == customer_id).first()

def get_all_customers(db: Session, skip: int = 0, limit: int = 100) -> List[Customer]:
    return db.query(Customer).offset(skip).limit(limit).all()

def create_customer(db: Session, customer_data: CustomerCreate) -> Customer:
    new_customer = Customer(**customer_data.model_dump())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def update_customer(db: Session, customer_id: int, customer_data: CustomerUpdate) -> Optional[Customer]:
    customer = get_customer(db, customer_id)
    if customer is None:
        return None
    for key, value in customer_data.model_dump(exclude_unset=True).items():
        setattr(customer, key, value)
    db.commit()
    db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int) -> bool:
    customer = get_customer(db, customer_id)
    if customer is None:
        return False
    db.delete(customer)
    db.commit()
    return True
