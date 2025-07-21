from sqlalchemy import Column, String, DateTime, Float
from app.models.base import Base
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    rating = Column(Float, nullable=False)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))