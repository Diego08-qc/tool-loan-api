from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import Optional
from fastapi import Query

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

#para el filtro, tenemos dos parametros opcionales (name,available)

@router.get("/", response_model=list[ToolResponse])
def read_tools(
    name: Optional[str] = Query(None),
    available: Optional[bool] = Query(None),
    db: Session = Depends(get_db),
):
    return get_tools(
        db,
        name=name,
        available=available,
    )

@router.get("/{tool_id}", response_model=ToolResponse)
def read_tool(
    tool_id: int,
    db: Session = Depends(get_db),
):
    return get_tool(db, tool_id)




@router.post("/", response_model=ToolResponse, status_code=201)
def create_new_tool(tool: ToolCreate, db: Session = Depends(get_db)):
    return create_tool(db, tool)


@router.put("/{tool_id}", response_model=ToolResponse)
def update_existing_tool(
    tool_id: int,
    tool: ToolUpdate,
    db: Session = Depends(get_db)
):
    return update_tool(db, tool_id, tool)



@router.delete("/{tool_id}")
def delete_existing_tool(tool_id: int, db: Session = Depends(get_db)):
    delete_tool(db, tool_id)
    return {"message": "Tool deleted successfully"}
