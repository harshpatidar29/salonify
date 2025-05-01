import enum
from sqlalchemy import Column, String, Integer, Enum, DateTime, Boolean
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy.orm import relationship
from datetime import date, time
from app.db.models.appointment_service import appointment_services


class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"

    
class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    duration = Column(time, nullable=True)
    gender = Column(Enum(Gender), default=Gender.other)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    appointments = relationship("Appointment", secondary=appointment_services, back_populates="services")