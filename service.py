from datetime import datetime
from typing import List, Optional
from models import Device, DeviceUpdate

class DeviceService:
    def __init__(self):
        self._storage: dict[int, Device] = {}
        self._counter: int = 1

    def create(self, device: Device) -> Device:
        device.id = self._counter
        device.created_at = datetime.now()
        self._storage[device.id] = device
        self._counter += 1
        return device
    
    def read_all(self) -> List[Device]:
        return list(self._storage.values())
    
    def read_by_id(self, device_id: int) -> Optional[Device]:
        return self._storage.get(device_id)
    
    def update(self, device_id: int, data: DeviceUpdate) -> Optional[Device]:
        device = self._storage.get(device_id)
        if device is None:
            return None
        device.name = data.name
        device.type = data.type
        device.room = data.room
        device.power_on = data.power_on
        device.value = data.value
        return device
    
    def delete(self, device_id: int) -> bool:
        if device_id in self._storage:
            del self._storage[device_id]
            return True
        return False

device_service = DeviceService()