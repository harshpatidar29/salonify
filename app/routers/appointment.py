from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.database import get_db
from app.crud import appointment_crud 
from app.schemas.appointments import AppointmentResponse, AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["Appointments"])


