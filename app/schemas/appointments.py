from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time, datetime
from enum import Enum


# --- Enum ---
class Status(str, Enum):
    pending = "pending"
    complete = "complete"
    cancel = "cancel"
    confirmed = "confirmed"


# --- Base shared fields ---
class AppointmentBase(BaseModel):
    user_id: int
    date: date
    time: time
    status: Status = Status.pending
    notes: Optional[str] = None


# --- Schema for creating an appointment ---
class AppointmentCreate(AppointmentBase):
    service_ids: List[int]


# --- Schema for reading appointment data ---
class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime
    service_ids: List[int]
    class Config:
        orm_mode = True