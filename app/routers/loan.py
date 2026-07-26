from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.loan import (
    create_loan,
    delete_loan,
    get_loan,
    get_loans,
    update_loan,
)
from app.db.database import get_db
from app.schemas.loan import LoanCreate, LoanResponse, LoanUpdate

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


@router.get("/", response_model=list[LoanResponse])
def read_loans(db: Session = Depends(get_db)):
    return get_loans(db)


@router.get("/{loan_id}", response_model=LoanResponse)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    loan = get_loan(db, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


@router.post("/", response_model=LoanResponse, status_code=201)
def create(loan: LoanCreate, db: Session = Depends(get_db)):
    return create_loan(db, loan)


@router.put("/{loan_id}", response_model=LoanResponse)
def update(loan_id: int, loan: LoanUpdate, db: Session = Depends(get_db)):
    updated = update_loan(db, loan_id, loan)
    if not updated:
        raise HTTPException(status_code=404, detail="Loan not found")
    return updated


@router.delete("/{loan_id}")
def delete(loan_id: int, db: Session = Depends(get_db)):
    deleted = delete_loan(db, loan_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Loan not found")
    return {"message": "Loan deleted successfully"}