from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.models.services import Service
from app.schemas.services import ServiceCreate, ServiceOut, ServiceUpdate
from passlib.context import CryptContext
from uuid import UUID

def get_service_by_salon(db: Session, salon_id: UUID, name: str):
    return db.query(Service).filter((Service.name == name) & (Service.salon_id == salon_id)).first()


def create_service(db: Session, service: ServiceCreate):
    db_service = Service(
        name=service.name,
        description=service.description,
        price=service.price,
        duration=service.duration,
        gender=service.gender,
        is_active=service.is_active,
        salon_id=service.salon_id,
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


def get_service_by_id(db: Session, service_id: int):
    return db.query(Service).filter(Service.id == service_id).first()

def get_all_service(db: Session):
    return db.query(Service).all()



def update_service(db: Session, service_id: int, service_data: ServiceUpdate):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        return None

    for field, value in service_data.dict(exclude_unset=True).items():
        setattr(service, field, value)

    db.commit()
    db.refresh(service)
    return service