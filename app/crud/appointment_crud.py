from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models.appointment import Appointment
from app.db.models.services import Service
from app.schemas.appointments import AppointmentCreate, AppointmentUpdate


def get_appointment_by_id(db:Session, id = int):
    return db.query(Appointment).filter(Appointment.id == id).first()


def get_all_appointment(db:Session):
    return db.query(Appointment).all()


def create_appointment(db: Session, appointment: AppointmentCreate):
    # Create appointment record
    db_appointment = Appointment(
        user_id=appointment.user_id,
        salon_id=appointment.salon_id,
        date=appointment.date,
        time=appointment.time,
        duration=appointment.duration,
        status=appointment.status,
        notes=appointment.notes,
        created_at=datetime.now()
    )

    # Add many-to-many services
    if appointment.services:
        db_services = db.query(Service).filter(Service.id.in_(appointment.services)).all()
        db_appointment.services = db_services

    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def update_appointment(db: Session, appointment_id: int, updates: AppointmentUpdate):
    db_appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not db_appointment:
        return None

    for field, value in updates.dict(exclude_unset=True).items():
        if field == "services":
            continue
        setattr(db_appointment, field, value)

    if updates.services is not None:
        db_services = db.query(Service).filter(Service.id.in_(updates.services)).all()
        db_appointment.services = db_services

    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def calculate_appointment_duration():
    pass