from pydantic import BaseModel
from typing import Optional
from datetime import  time, datetime
from enum import Enum


# --- Gender Enum (same as User model) ---
class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"


# --- Base shared fields ---
class ServiceBase(BaseModel):
    user_id: int
    name: str
    description: Optional[str] = None
    price: int
    duration: Optional[time] = None
    gender: Optional[Gender] = Gender.other
    is_active: Optional[bool] = True


# --- Schema for creating a service ---
class ServiceCreate(ServiceBase):
    pass


# --- Schema for reading service data ---
class ServiceOut(ServiceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    duration: Optional[time] = None
    gender: Optional[Gender] = None
    is_active: Optional[bool] = None

    class Config:
        orm_mode = True