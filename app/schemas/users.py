from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated, Optional
from enum import Enum
from datetime import datetime

PasswordStr = Annotated[str, StringConstraints(min_length=8)]

# --- Enum ---
class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class UserRole(str, Enum):
    owner = "owner"
    staff = "staff"
    customer = "customer"


# --- Base User Schema (shared fields) ---
class BaseUser(BaseModel):
    fullname: str
    username: str
    email: EmailStr
    phone: Optional[str] = None
    gender: Gender = Gender.other
    role: UserRole = UserRole.customer
    is_active: Optional[bool] = True


class UserCreate(BaseUser):
    password: PasswordStr


class UserResponse(BaseUser):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True