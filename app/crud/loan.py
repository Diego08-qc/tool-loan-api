from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.loan import LoanCreate, LoanUpdate


from app.models.loan import Loan
from app.models.tool import Tool
from app.models.borrower import Borrower


def get_loans(db: Session):
    return db.query(Loan).all()


def get_loan(db: Session, loan_id: int):
    return db.query(Loan).filter(Loan.id == loan_id).first()






def create_loan(db: Session, loan: LoanCreate):
    tool = db.query(Tool).filter(Tool.id == loan.tool_id).first()

    # REGLAS DE NEGOCIO:

        
    if not tool:

        #TIENE EXCEPCION SI NO SE ENCUENTRA LA HERRAMIENTA
        raise HTTPException(
        status_code=404,
        detail="Tool not found"
)
    if tool.quantity <= 0:

        # TIENE EXCEPCION SI NO HAY HERRAMIENTAS DISPONIBLES
        raise HTTPException(
        status_code=400,
        detail="Tool is not available"
)

    borrower = db.query(Borrower).filter(
        Borrower.id == loan.borrower_id
    ).first()

    if not borrower:

        # TIENE EXCEPCION SI NO SE ENCUENTRA EL PRESTATARIO
        raise HTTPException(
            status_code=404,
            detail="Borrower not found"
        )

    db_loan = Loan(**loan.model_dump())

    # ACTUALIZAR EL INVENTARIO
    tool.quantity -= 1

    if tool.quantity == 0:
        tool.available = False

    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


def update_loan(db: Session, loan_id: int, loan: LoanUpdate):
    db_loan = get_loan(db, loan_id)


    # REGLAS DE NEGOCIO: SI NO SE ENCUENTRA EL PRÉSTAMO, LANZAR UNA EXCEPCIÓN
    if not db_loan:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    for key, value in loan.model_dump(exclude_unset=True).items():
        setattr(db_loan, key, value)

    db.commit()
    db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, loan_id: int):
    db_loan = get_loan(db, loan_id)

    # REGLAS DE NEGOCIO: SI NO SE ENCUENTRA EL PRÉSTAMO, LANZAR UNA EXCEPCIÓN
    if not db_loan:
        raise HTTPException(
            status_code=404,
            detail="Loan not found"
        )

    #Devolver la herramienta al inventario al eliminar un préstamo

    tool = db.query(Tool).filter(
        Tool.id == db_loan.tool_id
    ).first()

    tool.quantity += 1
    tool.available = True

    db.delete(db_loan)
    db.commit()
    return db_loan