from pydantic import BaseModel

class ContractIncomeSummaryRead(BaseModel):
    contract_id: int
    total_payments: float
    total_fines: float
    total_income: float
