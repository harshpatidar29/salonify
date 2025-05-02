from sqlalchemy import Table, Column, ForeignKey

from app.db .database import Base

appointment_services = Table(
    "appointment_services",
    Base.metadata,
    Column("appointment_id", ForeignKey("appointments.id"), primary_key=True),
    Column("service_id", ForeignKey("services.id"), primary_key=True)
)
