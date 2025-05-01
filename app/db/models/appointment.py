from sqlalchemy import Column, String, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base
from datetime import date, time
from sqlalchemy.orm import relationship
from app.db.models.appointment_service import appointment_services
import enum


#Appointment model
class Status(str, enum.Enum):
    pending = "pending"
    complete = "complete"
    cancel = "cancel"
    confirmed = "confirmed"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(date, nullable=False)
    time = Column(time, nullable=False)
    duration = Column(time, nullable=True)
    status = Column(Enum(Status), default=Status.pending, nullable=False)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="appointments")

    # Many-to-many relationship to services
    services = relationship(
        "Service",
        secondary=appointment_services,
        back_populates="appointments"
    )