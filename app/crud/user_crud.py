from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.models.user import User
from app.schemas.users import UserCreate, UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_user(db: Session, user: UserCreate):
    db_user = User(
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        phone=user.phone,
        gender=user.gender,
        role=user.role,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, id: id):
    return db.query(User).filter(User.id == id).first()


def get_all_users(db: Session):
    return db.query(User).all()


def update_user(user_id: int, user_update: UserUpdate, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user
