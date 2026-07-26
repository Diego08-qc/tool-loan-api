from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud.borrower import (
    get_borrowers,
    get_borrower,
    create_borrower,
    update_borrower,
    delete_borrower,
)
from app.schemas.borrower import (
    BorrowerCreate,
    BorrowerUpdate,
    BorrowerResponse,
)

router = APIRouter(prefix="/borrowers", tags=["Borrowers"])


@router.get("/", response_model=list[BorrowerResponse])
def read_borrowers(db: Session = Depends(get_db)):
    return get_borrowers(db)


@router.get("/{borrower_id}", response_model=BorrowerResponse)
def read_borrower(borrower_id: int, db: Session = Depends(get_db)):
    borrower = get_borrower(db, borrower_id)

    if not borrower:
        raise HTTPException(status_code=404, detail="Borrower not found")

    return borrower


@router.post("/", response_model=BorrowerResponse, status_code=201)
def create_new_borrower(
    borrower: BorrowerCreate,
    db: Session = Depends(get_db)
):
    return create_borrower(db, borrower)


@router.put("/{borrower_id}", response_model=BorrowerResponse)
def update_existing_borrower(
    borrower_id: int,
    borrower: BorrowerUpdate,
    db: Session = Depends(get_db)
):
    updated = update_borrower(db, borrower_id, borrower)

    if not updated:
        raise HTTPException(status_code=404, detail="Borrower not found")

    return updated


@router.delete("/{borrower_id}")
def delete_existing_borrower(
    borrower_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_borrower(db, borrower_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Borrower not found")

    return {"message": "Borrower deleted successfully"}