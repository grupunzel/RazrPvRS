from fastapi import APIRouter, HTTPException, status, Header, Request
from fastapi.responses import HTMLResponse
from typing import List
from models import Device, DeviceUpdate, DeviceWithLinks, DeviceResponse, MessageResponse
from service import device_service
from translations import get_translation

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.post("/", response_model=DeviceResponse, status_code=status.HTTP_201_CREATED)
def create_device(device: Device, accept_language: str | None = Header(default=None, alias="Accept-Language")):
    _ = get_translation(accept_language)
    created = device_service.create(device)
    return DeviceResponse(message=_("device_created"), data=created)

@router.get("/", response_model=List[Device])
def get_all_devices():
    return device_service.read_all()

@router.get("/{device_id}", response_model=DeviceWithLinks)
def get_device(device_id: int, request: Request, accept_language: str | None = Header(default=None, alias="Accept-Language")):
    _ = get_translation(accept_language)
    device = device_service.read_by_id(device_id)
    if device is None:
        raise HTTPException(status_code=404, detail=_("device_not_found"))

    links = {
        _("link_self"):   str(request.url_for("get_device", device_id=device_id)),
        _("link_create"): str(request.url_for("create_device")),
        _("link_update"): str(request.url_for("update_device", device_id=device_id)),
        _("link_delete"): str(request.url_for("delete_device", device_id=device_id)),
    }
    return DeviceWithLinks(**device.model_dump(), links=links)

@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(device_id: int, data: DeviceUpdate, accept_language: str | None = Header(default=None, alias="Accept-Language")):
    _ = get_translation(accept_language)
    device = device_service.update(device_id, data)
    if device is None:
        raise HTTPException(status_code=404, detail=_("device_not_found"))
    return DeviceResponse(message=_("device_updated"), data=device)

@router.delete("/{device_id}", response_model=MessageResponse)
def delete_device(device_id: int, accept_language: str | None = Header(default=None, alias="Accept-Language")):
    _ = get_translation(accept_language)
    if not device_service.delete(device_id):
        raise HTTPException(status_code=404, detail=_("device_not_found"))
    return MessageResponse(message=_("device_deleted"))