from sqlalchemy import Column, Integer, String, Enum, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum
from app.db.models.appointment import Appointment  # Ensure correct import order


# user model
class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class UserRole(str, enum.Enum):
    owner = "owner"
    staff = "staff"
    customer = "customer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    gender = Column(Enum(Gender), default=Gender.other)
    role = Column(Enum(UserRole), default=UserRole.customer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    appointments = relationship("Appointment", back_populates="user")
    services = relationship("Service", back_populates="user")
    salons = relationship("Salon", back_populates="owner", cascade="all, delete")

