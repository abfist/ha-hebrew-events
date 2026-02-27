async def async_add_event(hass, call):
    storage = hass.data[DOMAIN]["storage"]

    new = {
        "id": str(uuid.uuid4()),
        "name": call.data["name"],
        "day": call.data["day"],
        "month": call.data["month"],
        "adar_type": call.data.get("adar_type", "auto"),
        "reminders": call.data.get("reminders", [])
    }

    storage.data.append(new)
    await storage.async_save()