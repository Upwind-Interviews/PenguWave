from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, DateTime, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

class Base(DeclarativeBase):
    """
    Declarative base class for SQLAlchemy models.
    Provides a common base for all database models in the application.
    """
    pass

class Event(Base):
    """
    Event model representing a security event as defined in docs/api_contract.md.
    
    Attributes:
        id (str): Unique identifier for the event (e.g., 'evt-001').
        timestamp (datetime): Timestamp of the event with timezone configuration.
        severity (str): Event severity level (e.g., 'INFO', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL').
        title (str): Title or summary of the event.
        description (str): Detailed description of the security event.
        asset_hostname (str): Hostname of the affected asset.
        asset_ip (str): IP address of the affected asset.
        source_ip (str): Originating IP address of the threat/action.
        tags (List[str]): List of custom tags/labels assigned to this event.
    """
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    severity: Mapped[str] = mapped_column(String, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    asset_hostname: Mapped[Optional[str]] = mapped_column("asset_hostname", String, nullable=True)
    asset_ip: Mapped[Optional[str]] = mapped_column("asset_ip", String, nullable=True)
    source_ip: Mapped[Optional[str]] = mapped_column("source_ip", String, nullable=True)
    
    # Explicitly use the PostgreSQL dialect ARRAY type to store tags efficiently
    tags: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=False, default=list)

    def __repr__(self) -> str:
        return f"<Event(id={self.id!r}, title={self.title!r}, severity={self.severity!r})>"
