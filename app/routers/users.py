from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserResponse, UserUpdate
from app.crud import user_crud as crud_user
from app.db.database import get_db
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/",response_model=UserResponse)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db, user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    db_user = crud_user.get_user_by_id(db, id = user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User Not Found")
    return db_user


@router.get("/all_user/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    db_users = crud_user.get_all_users(db)
    if not db_users:
        raise HTTPException(status_code=400, detail="No User Found")
    return db_users


@router.delete("/{user_id}")
def delete_user(user_id, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_id(db, id = user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User Not Found")
    db.delete(db_user)
    db.commit()
    return {"detail": f"User with id {user_id} deleted successfully"}


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return crud_user.update_user(user_id, user_update, db)
