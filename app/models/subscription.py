from sqlalchemy import Column, String, DateTime
from app.models.base import Base
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    plan = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))
