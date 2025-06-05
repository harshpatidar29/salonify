import enum
from sqlalchemy import Column, String, Integer, Enum, DateTime, Boolean, Time, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy.orm import relationship
from app.db.models.appointment_service import appointment_services
from sqlalchemy.dialects.postgresql import UUID

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
    duration = Column(Time, nullable=True)
    gender = Column(Enum(Gender), default=Gender.other, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    salon_id = Column(UUID(as_uuid=True), ForeignKey("salons.id"), nullable=False)

    salon = relationship("Salon", back_populates="services")

    appointments = relationship(
        "Appointment", secondary=appointment_services, back_populates="services"
    )
