from sqlalchemy.orm import Session
from uuid import UUID
from app.db.models.staff import StaffMember
from app.schemas.staff import StaffMemberCreate, StaffMemberUpdate


def create_staff_member(db: Session, staff: StaffMemberCreate) -> StaffMember:
    db_staff = StaffMember(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff


def get_staff_member(db: Session, staff_id: UUID) -> StaffMember:
    return db.query(StaffMember).filter(StaffMember.id == staff_id).first()


def get_staff_by_salon(db: Session, salon_id: UUID):
    return db.query(StaffMember).filter(StaffMember.salon_id == salon_id).all()


def update_staff_member(db: Session, staff_id: UUID, staff_data: StaffMemberUpdate) -> StaffMember:
    db_staff = db.query(StaffMember).filter(StaffMember.id == staff_id).first()
    if not db_staff:
        return None
    for key, value in staff_data.dict(exclude_unset=True).items():
        setattr(db_staff, key, value)
    db.commit()
    db.refresh(db_staff)
    return db_staff


def delete_staff_member(db: Session, staff_id: UUID) -> bool:
    staff = db.query(StaffMember).filter(StaffMember.id == staff_id).first()
    if not staff:
        return False
    db.delete(staff)
    db.commit()
    return True
