from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID
from .users import BaseUser

class StaffMemberBase(BaseModel):
    role: str
    image_url: Optional[str] = None
    is_active: Optional[bool] = True


class StaffMemberCreate(StaffMemberBase):
    salon_id: UUID
    user_id: int


class StaffMemberUpdate(StaffMemberBase):
    role: Optional[str] = None
    image_url: Optional[str] = None
    is_active: Optional[bool] = None
    salon_id: Optional[UUID] = None


class StaffMemberOut(StaffMemberBase):
    id: UUID
    salon_id: UUID
    user: BaseUser

    class Config:
        orm_mode = True
