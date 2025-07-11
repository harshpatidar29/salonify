from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.staff import StaffMemberCreate, StaffMemberUpdate, StaffMemberOut
from app.crud import staff as crud_staff
from app.db.database import get_db
from app.core.dependencies import get_current_user
from app.db.models.user import User

router = APIRouter()


@router.post("/staff/", response_model=StaffMemberOut, status_code=status.HTTP_201_CREATED)
def create_staff(
    staff: StaffMemberCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_staff.create_staff_member(db, staff)


@router.get("/staff/{staff_id}", response_model=StaffMemberOut)
def read_staff_member(
    staff_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_staff = crud_staff.get_staff_member(db, staff_id)
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return db_staff


@router.put("/staff/{staff_id}", response_model=StaffMemberOut)
def update_staff(
    staff_id: UUID,
    staff_update: StaffMemberUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = crud_staff.update_staff_member(db, staff_id, staff_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Staff member not found")
    return updated


@router.delete("/staff/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff(
    staff_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = crud_staff.delete_staff_member(db, staff_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Staff member not found")


@router.get("/SalonStaff/{salon_id}", response_model=list[StaffMemberOut])
def read_staff_by_salon(
    salon_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_staff.get_staff_by_salon(db, salon_id)