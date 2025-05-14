from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID


class StaffMemberBase(BaseModel):
    name: str
    role: str
    bio: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = True


class StaffMemberCreate(StaffMemberBase):
    salon_id: UUID


class StaffMemberUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    bio: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None


class StaffMemberOut(StaffMemberBase):
    id: UUID
    salon_id: UUID

    class Config:
        orm_mode = True
