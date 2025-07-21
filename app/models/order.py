from sqlalchemy import Column, String, DateTime, JSON, Float
from app.models.base import Base
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey

class Order(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    table_id = Column(String, nullable=False)
    items = Column(JSON, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="pending", nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))
