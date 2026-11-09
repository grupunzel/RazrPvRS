TRANSLATIONS = {
    "ru": {
        "device_created": "Устройство успешно создано",
        "device_updated": "Устройство успешно обновлено",
        "device_deleted": "Устройство успешно удалено",
        "device_not_found": "Устройство не найдено",
        "link_self": "получить",
        "link_create": "создать",
        "link_update": "обновить",
        "link_delete": "удалить",
    },
    "en": {
        "device_created": "Device created successfully",
        "device_updated": "Device updated successfully",
        "device_deleted": "Device deleted successfully",
        "device_not_found": "Device not found",
        "link_self": "self",
        "link_create": "create",
        "link_update": "update",
        "link_delete": "delete",
    },
    "es": {
        "device_created": "Dispositivo creado exitosamente",
        "device_updated": "Dispositivo actualizado exitosamente",
        "device_deleted": "Dispositivo eliminado exitosamente",
        "device_not_found": "Dispositivo no encontrado",
        "link_self": "obtener",
        "link_create": "crear",
        "link_update": "actualizar",
        "link_delete": "eliminar",
    }
}

DEFAULT_LANG = "ru"

def get_translation(accept_language: str | None):
    lang = DEFAULT_LANG
    if accept_language:
        preferred = accept_language.split(',')[0].split('-')[0].strip().lower()
        if preferred in TRANSLATIONS:
            lang = preferred
    
    def translate(key: str) -> str:
        return TRANSLATIONS.get(lang, TRANSLATIONS[DEFAULT_LANG]).get(key, key)
    
    return translate
