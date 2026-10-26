from fastapi import APIRouter, HTTPException, status
from fastapi.responses import HTMLResponse
from typing import List
from models import Device, DeviceUpdate
from service import device_service

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.post("/", response_model=Device, status_code=status.HTTP_201_CREATED)
def create_device(device: Device):
    return device_service.create(device)

@router.get("/", response_model=List[Device])
def get_all_devices():
    return device_service.read_all()

@router.get("/{device_id}", response_model=Device)
def get_device(device_id: int):
    d = device_service.read_by_id(device_id)
    if d is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return d

@router.put("/{device_id}", response_model=Device)
def update_device(device_id: int, data: DeviceUpdate):
    device = device_service.update(device_id, data)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_device(device_id: int):
    if not device_service.delete(device_id):
        raise HTTPException(status_code=404, detail="Device not found")
    return None