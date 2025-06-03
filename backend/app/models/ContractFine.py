from sqlalchemy import Column, ForeignKey, Integer
from db import Base

class ContractFine(Base):
    __tablename__ = 'contract_fine'
    rental_contract_id = Column(Integer, ForeignKey("rentalcontract.id"), primary_key=True)
    fine_id = Column(Integer, ForeignKey("fine.id"), primary_key=True)