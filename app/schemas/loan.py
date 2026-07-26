from datetime import date
from pydantic import BaseModel


class LoanBase(BaseModel):
    tool_id: int
    borrower_id: int
    loan_date: date
    return_date: date | None = None
    returned: bool = False


class LoanCreate(LoanBase):
    pass


class LoanUpdate(BaseModel):
    tool_id: int | None = None
    borrower_id: int | None = None
    loan_date: date | None = None
    return_date: date | None = None
    returned: bool | None = None


class LoanResponse(LoanBase):
    id: int

    model_config = {
        "from_attributes": True
    }