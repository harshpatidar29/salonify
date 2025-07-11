from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid
from .timeslot import TimeSlot

class StaffMember(Base):
    __tablename__ = "staff_members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    salon_id = Column(UUID(as_uuid=True), ForeignKey("salons.id"), nullable=False)

    role = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="staff_profile")
    salon = relationship("Salon", back_populates="staff_members")
    time_slots = relationship("TimeSlot", back_populates="staff_member")
