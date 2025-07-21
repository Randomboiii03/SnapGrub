from pydantic import BaseModel
from typing import Optional

class MenuItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: str
    image_url: Optional[str] = None
    
class MenuCategoryCreate(BaseModel):
    name: str