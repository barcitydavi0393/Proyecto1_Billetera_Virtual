from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    password: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    phone: str
    amount: float

    class Config:
        from_attributes = True
