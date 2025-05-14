from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.salon import SalonCreate, SalonUpdate, SalonOut
from app.crud.salon import create_salon, get_salon, get_salons, update_salon, delete_salon
from uuid import UUID
from app.core.dependencies import get_current_user


router = APIRouter(prefix="/salons", tags=["salons"])


@router.post("/", response_model=SalonOut)
def create_salon_view(
    salon: SalonCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    owner_id = current_user.id
    return create_salon(db=db, salon=salon, owner_id=owner_id)


@router.get("/{salon_id}", response_model=SalonOut)
def get_salon_view(salon_id: UUID, db: Session = Depends(get_db)):
    db_salon = get_salon(db=db, salon_id=salon_id)
    if db_salon is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Salon not found")
    return db_salon


@router.get("/", response_model=list[SalonOut])
def get_salons_view(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_salons(db=db, skip=skip, limit=limit)


@router.put("/{salon_id}", response_model=SalonOut)
def update_salon_view(salon_id: UUID, salon: SalonUpdate, db: Session = Depends(get_db)):
    db_salon = update_salon(db=db, salon_id=salon_id, salon=salon)
    if db_salon is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Salon not found")
    return db_salon


@router.delete("/{salon_id}", response_model=SalonOut)
def delete_salon_view(salon_id: UUID, db: Session = Depends(get_db)):
    db_salon = delete_salon(db=db, salon_id=salon_id)
    if db_salon is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Salon not found")
    return db_salon
