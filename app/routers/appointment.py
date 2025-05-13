from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.crud import appointment_crud 
from app.schemas.appointments import AppointmentResponse, AppointmentCreate, AppointmentUpdate

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.get("/{appointment_id}/", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = appointment_crud.get_appointment_by_id(db, id=appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=400, detail="Appointment Not Found")
    return db_appointment

@router.get("/", response_model=list[AppointmentResponse])
def get_all_appointment( db: Session = Depends(get_db)):
    db_appointment = appointment_crud.get_all_appointment(db)
    if not db_appointment:
        raise HTTPException(status_code=400, detail="Appointment Not Found")
    return db_appointment


@router.post("/", response_model=AppointmentResponse)
def create_appointment_api(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    try:
        return appointment_crud.create_appointment(db=db, appointment=appointment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating appointment: {str(e)}")
    

@router.delete("/{appointment_id}/", status_code=200)
def delete_appointment(appointment_id = int, db: Session = Depends(get_db)):
    db_appointment = appointment_crud.get_appointment_by_id(db, id=appointment_id)
    if not db_appointment:
        raise HTTPException(status_code=400, detail="Appointment Not Found")
    db.delete(db_appointment)
    db.commit()
    return {"detail": f"appointment with id {appointment_id} deleted successfully"}


@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment_api(appointment_id: int,updates: AppointmentUpdate,db: Session = Depends(get_db)):
    updated_appointment = appointment_crud.update_appointment(db=db, appointment_id=appointment_id, updates=updates)
    if not updated_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return updated_appointment


@router.get("/available_slot/{woner_id}/")
def get_available_appointment(owner_id: int, db: Session = Depends(get_db)):
    available_appointments = appointment_crud.get_available_appointment(db, owner_id=owner_id)
    return True