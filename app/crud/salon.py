from sqlalchemy.orm import Session
from app.db.models.salon import Salon
from app.schemas.salon import SalonCreate, SalonUpdate
from app.core.security import hash_password
from uuid import UUID


def create_salon(db: Session, salon: SalonCreate, owner_id: int) -> Salon:
    db_salon = Salon(
        name=salon.name,
        description=salon.description,
        phone=salon.phone,
        email=salon.email,
        address=salon.address,
        city=salon.city,
        state=salon.state,
        zip_code=salon.zip_code,
        owner_id=owner_id
    )
    db.add(db_salon)
    db.commit()
    db.refresh(db_salon)
    return db_salon


def get_salon(db: Session, salon_id: UUID) -> Salon:
    return db.query(Salon).filter(Salon.id == salon_id).first()


def get_salons(db: Session, skip: int = 0, limit: int = 100) -> list[Salon]:
    return db.query(Salon).offset(skip).limit(limit).all()


def update_salon(db: Session, salon_id: UUID, salon: SalonUpdate) -> Salon:
    db_salon = db.query(Salon).filter(Salon.id == salon_id).first()
    if db_salon:
        for key, value in salon.dict(exclude_unset=True).items():
            setattr(db_salon, key, value)
        db.commit()
        db.refresh(db_salon)
    return db_salon


def delete_salon(db: Session, salon_id: UUID) -> Salon:
    db_salon = db.query(Salon).filter(Salon.id == salon_id).first()
    if db_salon:
        db.delete(db_salon)
        db.commit()
    return db_salon
