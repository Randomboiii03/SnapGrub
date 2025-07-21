from sqlalchemy import Column, String, DateTime
from app.models.base import Base
import uuid
from datetime import datetime

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))
    
