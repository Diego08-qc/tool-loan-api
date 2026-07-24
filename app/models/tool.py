from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Tool(Base):
    __tablename__ = "tools"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    category: Mapped[str] = mapped_column(String(100), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, default=0)

    available: Mapped[bool] = mapped_column(Boolean, default=True)