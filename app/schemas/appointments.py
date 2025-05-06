from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time, datetime
from enum import Enum


# Status Enum
class AppointmentStatus(str, Enum):
    pending = "pending"
    complete = "complete"
    cancel = "cancel"
    confirmed = "confirmed"


# Minimal Service Schema for output
class ServiceOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class AppointmentCreate(BaseModel):
    user_id: int
    date: date
    duration: Optional[time] = None
    time: time
    status: AppointmentStatus = AppointmentStatus.pending
    notes: Optional[str] = None
    services: Optional[List[int]] = []

    class Config:
        orm_mode = True


class AppointmentResponse(BaseModel):
    id: int
    duration: Optional[time]
    user_id: int
    date: date
    time: time
    status: AppointmentStatus
    notes: Optional[str]
    created_at: datetime
    services: List[ServiceOut]

    class Config:
        orm_mode = True


class AppointmentUpdate(BaseModel):
    user_id: int
    duration: Optional[time]
    date: Optional[date]
    time: Optional[time]
    status: Optional[AppointmentStatus]
    notes: Optional[str]
    services: Optional[List[int]]

    class Config:
        orm_mode = True