from pydantic import BaseModel


class ToolBase(BaseModel):
    name: str
    category: str
    quantity: int
    available: bool = True


class ToolCreate(ToolBase):
    pass


class ToolUpdate(ToolBase):
    pass


class ToolResponse(ToolBase):
    id: int

    class Config:
        from_attributes = True