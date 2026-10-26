from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Device(BaseModel):
    id: Optional[int] = Field(default=None, description="Уникальный идентификатор")
    name: str = Field(..., description="Название устройства")
    type: str = Field(..., description="Тип: LIGHT, THERMOSTAT, SENSOR")
    room: str = Field(..., description="Комната размещения")
    power_on: bool = Field(default=False, description="Состояние вкл/выкл")
    value: float = Field(default=0.0, description="Значение температуры")
    created_at: Optional[datetime] = Field(default=None, description="Дата добавления")

class DeviceUpdate(BaseModel):
    name: str
    type: str
    room: str
    power_on: bool
    value: float