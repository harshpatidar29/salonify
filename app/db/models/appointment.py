from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey, Time, Date
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy.orm import relationship
from app.db.models.appointment_service import appointment_services
from app.db.models.services import Service
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum


# Appointment model
class Status(str, enum.Enum):
    pending = "pending"
    complete = "complete"
    cancel = "cancel"
    confirmed = "confirmed"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    salon_id = Column(UUID(as_uuid=True), ForeignKey("salons.id"), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    duration = Column(Time, nullable=True)
    status = Column(Enum(Status), default=Status.pending, nullable=False)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="appointments")
    salon = relationship("Salon", back_populates="appointments")
    # Many-to-many relationship to services
    services = relationship(
        "Service", secondary=appointment_services, back_populates="appointments"
    )
