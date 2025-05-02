from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time, datetime
from enum import Enum


# --- Gender Enum (same as User model) ---
class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"


# --- Base shared fields ---
class ServiceBase(BaseModel):
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