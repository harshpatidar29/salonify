import enum
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Integer, DECIMAL, Enum, DateTime
from sqlalchemy.orm import relationship
from app.db.database import Base


class PaymentMethodEnum(str, enum.Enum):
    card = "card"
    cash = "cash"
    online = "online"


class PaymentStatusEnum(str, enum.Enum):
    pending = 'pending'
    paid = 'paid'
    failed = 'failed'


class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_method = Column(Enum(PaymentMethodEnum), nullable=False)
    status = Column(Enum(PaymentStatusEnum), nullable=False, default=PaymentStatusEnum.pending)
    transaction_id = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    appointment = relationship("Appointment", back_populates="payment")
    user = relationship("User", back_populates="payments")