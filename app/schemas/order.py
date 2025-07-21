from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    item_id: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    table_id: str
    items: List[OrderItem]
    total_amount: float
