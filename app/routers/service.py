from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.services import ServiceCreate, ServiceOut, ServiceUpdate
from app.crud import service_crud
from app.db.database import get_db

router = APIRouter(prefix="/service", tags=["service"])

@router.post("/", response_model=ServiceOut)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    db_service = service_crud.get_service_by_salon(db, salon_id=service.salon_id, name=service.name)
    if db_service:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service_crud.create_service(db, service)

@router.get("/all_service/", response_model=list[ServiceOut])
def get_all_Service(db: Session = Depends(get_db)):
    db_service = service_crud.get_all_service(db)
    if not db_service:
        raise HTTPException(status_code=400, detail="Service Not Found")
    return db_service


@router.get("/{service_id}/", response_model=ServiceOut)
def get_service(service_id: int, db: Session = Depends(get_db)):
    db_service = service_crud.get_service_by_id(db, service_id=service_id)
    if not db_service:
        raise HTTPException(status_code=400, detail="Service Not Found")
    return db_service


@router.delete("/{service_id}")
def delete_service(service_id:int, db: Session = Depends(get_db)):
    db_service = service_crud.get_service_by_id(db, service_id=service_id)
    if not db_service:
        raise HTTPException(status_code=400, detail="Service Not Found")
    db.delete(db_service)
    db.commit()
    return {"detail": f"Service with id {service_id} deleted successfully"}


@router.patch("/{service_id}", response_model=ServiceUpdate)
def patch_service(service_id: int, service_data: ServiceUpdate, db: Session = Depends(get_db)):
    service = service_crud.update_service(db, service_id, service_data)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
