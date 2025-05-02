from fastapi import FastAPI
from sqlalchemy.orm import declarative_base

Base = declarative_base()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Salonify API!"}