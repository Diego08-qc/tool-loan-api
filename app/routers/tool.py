from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.tool import (
    create_tool,
    delete_tool,
    get_tool,
    get_tools,
    update_tool,
)
from app.db.database import get_db
from app.schemas.tool import ToolCreate, ToolResponse, ToolUpdate

router = APIRouter(
    prefix="/tools",
    tags=["Tools"]
)


@router.get("/", response_model=list[ToolResponse])
def read_tools(db: Session = Depends(get_db)):
    return get_tools(db)


@router.get("/{tool_id}", response_model=ToolResponse)
def read_tool(tool_id: int, db: Session = Depends(get_db)):
    tool = get_tool(db, tool_id)

    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    return tool


@router.post("/", response_model=ToolResponse, status_code=201)
def create_new_tool(tool: ToolCreate, db: Session = Depends(get_db)):
    return create_tool(db, tool)


@router.put("/{tool_id}", response_model=ToolResponse)
def update_existing_tool(
    tool_id: int,
    tool: ToolUpdate,
    db: Session = Depends(get_db)
):
    updated_tool = update_tool(db, tool_id, tool)

    if not updated_tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    return updated_tool


@router.delete("/{tool_id}")
def delete_existing_tool(tool_id: int, db: Session = Depends(get_db)):
    deleted_tool = delete_tool(db, tool_id)

    if not deleted_tool:
        raise HTTPException(status_code=404, detail="Tool not found")

    return {"message": "Tool deleted successfully"}