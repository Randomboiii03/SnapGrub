from sqlalchemy import Column, String, DateTime, Float, Boolean
from app.models.base import Base
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey

class MenuCategory(Base):
    __tablename__ = "menu_categories"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    category_id = Column(String, ForeignKey("menu_categories.id"), nullable=False)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    image_url = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(datetime.timezone.utc), onupdate=datetime.now(datetime.timezone.utc))