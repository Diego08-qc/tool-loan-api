from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.borrower import Borrower
from app.schemas.borrower import BorrowerCreate, BorrowerUpdate


def get_borrowers(db: Session):
    return db.query(Borrower).all()


def get_borrower(db: Session, borrower_id: int):
    return db.query(Borrower).filter(Borrower.id == borrower_id).first()


def create_borrower(db: Session, borrower: BorrowerCreate):
    db_borrower = Borrower(**borrower.model_dump())

    db.add(db_borrower)
    db.commit()
    db.refresh(db_borrower)

    return db_borrower


def update_borrower(db: Session, borrower_id: int, borrower: BorrowerUpdate):
    db_borrower = get_borrower(db, borrower_id)

    if not db_borrower:
        raise HTTPException(
            status_code=404,
            detail="Borrower not found"
    )

    for key, value in borrower.model_dump().items():
        setattr(db_borrower, key, value)

    db.commit()
    db.refresh(db_borrower)

    return db_borrower


def delete_borrower(db: Session, borrower_id: int):
    db_borrower = get_borrower(db, borrower_id)

    if not db_borrower:
        raise HTTPException(
            status_code=404,
            detail="Borrower not found"
    )

    db.delete(db_borrower)
    db.commit()

    return db_borrower