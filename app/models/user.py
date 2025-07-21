from sqlalchemy import Column, String, DateTime
from app.models.base import Base
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))
    