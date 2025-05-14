from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid


class StaffMember(Base):
    __tablename__ = "staff_members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    salon_id = Column(UUID(as_uuid=True), ForeignKey("salons.id"), nullable=False)

    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    bio = Column(String)
    phone = Column(String)
    email = Column(String)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    salon = relationship("Salon", back_populates="staff_members")
