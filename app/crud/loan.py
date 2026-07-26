from sqlalchemy.orm import Session

from app.models.loan import Loan
from app.schemas.loan import LoanCreate, LoanUpdate


def get_loans(db: Session):
    return db.query(Loan).all()


def get_loan(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()


def create_loan(db: Session, loan: LoanCreate):
    db_loan = Loan(**loan.model_dump())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def update_loan(db: Session, loan_id: int, loan: LoanUpdate):
    db_loan = get_loan(db, loan_id)

    if not db_loan:
        return None

    for key, value in loan.model_dump(exclude_unset=True).items():
        setattr(db_loan, key, value)

    db.commit()
    db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, loan_id: int):
    db_loan = get_loan(db, loan_id)

    if not db_loan:
        return None

    db.delete(db_loan)
    db.commit()
    return db_loan