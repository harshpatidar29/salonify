from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from app.routers import users, service

Base = declarative_base()

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Salonify API!"}


app.include_router(users.router)
app.include_router(service.router)
