from sqlalchemy.orm import Session
from fastapi import HTTPException

from typing import Optional

from app.models.tool import Tool
from app.schemas.tool import ToolCreate, ToolUpdate


def get_tools(
    db: Session,
    name: Optional[str] = None,
    available: Optional[bool] = None,
):
    query = db.query(Tool)

    if name:
        query = query.filter(Tool.name.ilike(f"%{name}%"))

    if available is not None:
        if available:
            query = query.filter(Tool.quantity > 0)
        else:
            query = query.filter(Tool.quantity == 0)

    return query.all()


def get_tool(db: Session, tool_id: int):
    tool = db.query(Tool).filter(Tool.id == tool_id).first()

    if not tool:
        raise HTTPException(
            status_code=404,
            detail="Tool not found"
        )

    return tool


def create_tool(db: Session, tool: ToolCreate):
    db_tool = Tool(**tool.model_dump())

    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)

    return db_tool


def update_tool(db: Session, tool_id: int, tool: ToolUpdate):
    db_tool = get_tool(db, tool_id)

    for key, value in tool.model_dump().items():
        setattr(db_tool, key, value)

    db.commit()
    db.refresh(db_tool)

    return db_tool


def delete_tool(db: Session, tool_id: int):
    db_tool = get_tool(db, tool_id)

    db.delete(db_tool)
    db.commit()

    return db_tool