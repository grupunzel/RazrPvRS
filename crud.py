from typing import List, Optional

from sqlalchemy.orm import Session

from db_models import DeviceDB
from models import Device, DeviceUpdate


def create(db: Session, device: Device) -> DeviceDB:
    db_device = DeviceDB(
        name=device.name,
        type=device.type,
        room=device.room,
        power_on=device.power_on,
        value=device.value,
    )
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_all(db: Session) -> List[DeviceDB]:
    return db.query(DeviceDB).order_by(DeviceDB.id).all()


def get_by_id(db: Session, device_id: int) -> Optional[DeviceDB]:
    return db.get(DeviceDB, device_id)


def update(db: Session, device_id: int, data: DeviceUpdate) -> Optional[DeviceDB]:
    db_device = db.get(DeviceDB, device_id)
    if db_device is None:
        return None
    db_device.name = data.name
    db_device.type = data.type
    db_device.room = data.room
    db_device.power_on = data.power_on
    db_device.value = data.value
    db.commit()
    db.refresh(db_device)
    return db_device


def delete(db: Session, device_id: int) -> bool:
    db_device = db.get(DeviceDB, device_id)
    if db_device is None:
        return False
    db.delete(db_device)
    db.commit()
    return True