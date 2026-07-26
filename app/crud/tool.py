from sqlalchemy.orm import Session

from app.models.tool import Tool
from app.schemas.tool import ToolCreate, ToolUpdate


def get_tools(db: Session):
    return db.query(Tool).all()


def get_tool(db: Session, tool_id: int):
    return db.query(Tool).filter(Tool.id == tool_id).first()


def create_tool(db: Session, tool: ToolCreate):
    db_tool = Tool(**tool.model_dump())

    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)

    return db_tool


def update_tool(db: Session, tool_id: int, tool: ToolUpdate):
    db_tool = get_tool(db, tool_id)

    if not db_tool:
        return None

    for key, value in tool.model_dump().items():
        setattr(db_tool, key, value)

    db.commit()
    db.refresh(db_tool)

    return db_tool


def delete_tool(db: Session, tool_id: int):
    db_tool = get_tool(db, tool_id)

    if not db_tool:
        return None

    db.delete(db_tool)
    db.commit()

    return db_tool