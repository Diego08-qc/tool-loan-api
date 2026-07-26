from pydantic import BaseModel


class BorrowerBase(BaseModel):
    name: str
    email: str
    phone: str


class BorrowerCreate(BorrowerBase):
    pass


class BorrowerUpdate(BorrowerBase):
    pass


class BorrowerResponse(BorrowerBase):
    id: int

    model_config = {
        "from_attributes": True
    }