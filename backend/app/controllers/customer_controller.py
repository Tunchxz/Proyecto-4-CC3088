from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.Customer import CustomerCreate, CustomerRead, CustomerUpdate
from services.customer_service import (
    get_customer, get_all_customers, create_customer, update_customer, delete_customer
)
from db import get_db
from typing import List

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=List[CustomerRead])
def list_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_customers(db, skip, limit)

@router.get("/{customer_id}", response_model=CustomerRead)
def retrieve_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_new_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db, customer)

@router.put("/{customer_id}", response_model=CustomerRead)
def update_existing_customer(customer_id: int, update_data: CustomerUpdate, db: Session = Depends(get_db)):
    customer = update_customer(db, customer_id, update_data)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_customer(customer_id: int, db: Session = Depends(get_db)):
    success = delete_customer(db, customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
