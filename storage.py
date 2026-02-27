from homeassistant.helpers.storage import Store
from .const import STORAGE_KEY, STORAGE_VERSION

class HebrewEventStorage:

    def __init__(self, hass):
        self.store = Store(hass, STORAGE_VERSION, STORAGE_KEY)
        self.data = []

    async def async_load(self):
        self.data = await self.store.async_load() or []

    async def async_save(self):
        await self.store.async_save(self.data)