from pydantic import BaseModel
from typing import Optional


class FeedbackCreate(BaseModel):
    rating: int
    comment: Optional[str] = None
