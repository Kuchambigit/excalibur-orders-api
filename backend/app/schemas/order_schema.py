from pydantic import BaseModel

class OrderSchema(BaseModel):
    order_id: int
    order_date: str
    amount: float
    description: str


