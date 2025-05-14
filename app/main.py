from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from app.routers import users, service, appointment, auth, protected, salon, staff
from fastapi.middleware.cors import CORSMiddleware

Base = declarative_base()

app = FastAPI()

# Allow frontend origin (React)
origins = [
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Salonify API!"}


app.include_router(users.router)
app.include_router(service.router)
app.include_router(appointment.router)
app.include_router(salon.router)
app.include_router(staff.router)

app.include_router(auth.router)
app.include_router(protected.router)
