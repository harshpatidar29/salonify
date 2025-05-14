from pydantic import BaseModel, EmailStr, UUID4
from typing import Optional
from datetime import datetime


class SalonBase(BaseModel):
    name: str
    description: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None


class SalonCreate(SalonBase):
    pass


class SalonUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    is_approved: Optional[bool] = None


class SalonOut(SalonBase):
    id: UUID4
    owner_id: int
    is_approved: bool
    created_at: datetime

    class Config:
        orm_mode = True
