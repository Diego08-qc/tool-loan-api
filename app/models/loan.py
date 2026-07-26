from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer
from app.db.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    tool_id = Column(Integer, ForeignKey("tools.id"), nullable=False)
    borrower_id = Column(Integer, ForeignKey("borrowers.id"), nullable=False)
    loan_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    returned = Column(Boolean, default=False)