from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, String, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class DeviceDB(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    room: Mapped[str] = mapped_column(String(100), nullable=False)
    power_on: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    value: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )