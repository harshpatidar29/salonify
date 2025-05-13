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
    full_name: str
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


class UserUpdate(BaseModel):
    full_name: Optional[str]
    username: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    gender: Optional[Gender]
    role: Optional[UserRole]
    is_active: Optional[bool]


class UserFilter(BaseModel):
    id: Optional[int] = None
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    gender: Optional[Gender] =  None
    role: Optional[UserRole] = None
    