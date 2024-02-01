from pydantic import BaseModel


class CarCreate(BaseModel):
    brand: str
    model: str
    price: int
    color: str
    user_id: int