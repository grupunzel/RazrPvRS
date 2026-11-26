from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from sqlalchemy.orm import Session
from typing import List

import crud
from database import get_db
from models import (
    Device,
    DeviceResponse,
    DeviceUpdate,
    DeviceWithLinks,
    MessageResponse,
)
from translations import get_translation

router = APIRouter(prefix="/api/devices", tags=["Devices"])


@router.post("/", response_model=DeviceResponse, status_code=status.HTTP_201_CREATED)
def create_device(
    device: Device,
    db: Session = Depends(get_db),
    accept_language: str | None = Header(default=None, alias="Accept-Language"),
):
    _ = get_translation(accept_language)
    created = crud.create(db, device)
    return DeviceResponse(message=_("device_created"), data=created)


@router.get("/", response_model=List[Device])
def get_all_devices(db: Session = Depends(get_db)):
    return crud.get_all(db)


@router.get("/{device_id}", response_model=DeviceWithLinks)
def get_device(
    device_id: int,
    request: Request,
    db: Session = Depends(get_db),
    accept_language: str | None = Header(default=None, alias="Accept-Language"),
):
    _ = get_translation(accept_language)
    device = crud.get_by_id(db, device_id)
    if device is None:
        raise HTTPException(status_code=404, detail=_("device_not_found"))

    device_pydantic = Device.model_validate(device)
    links = {
        _("link_self"): str(request.url_for("get_device", device_id=device_id)),
        _("link_create"): str(request.url_for("create_device")),
        _("link_update"): str(request.url_for("update_device", device_id=device_id)),
        _("link_delete"): str(request.url_for("delete_device", device_id=device_id)),
    }
    return DeviceWithLinks(**device_pydantic.model_dump(), links=links)


@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(
    device_id: int,
    data: DeviceUpdate,
    db: Session = Depends(get_db),
    accept_language: str | None = Header(default=None, alias="Accept-Language"),
):
    _ = get_translation(accept_language)
    device = crud.update(db, device_id, data)
    if device is None:
        raise HTTPException(status_code=404, detail=_("device_not_found"))
    return DeviceResponse(message=_("device_updated"), data=device)


@router.delete("/{device_id}", response_model=MessageResponse)
def delete_device(
    device_id: int,
    db: Session = Depends(get_db),
    accept_language: str | None = Header(default=None, alias="Accept-Language"),
):
    _ = get_translation(accept_language)
    if not crud.delete(db, device_id):
        raise HTTPException(status_code=404, detail=_("device_not_found"))
    return MessageResponse(message=_("device_deleted"))