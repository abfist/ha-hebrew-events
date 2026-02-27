from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from datetime import timedelta

class HebrewEventsCoordinator(DataUpdateCoordinator):

    def __init__(self, hass):
        super().__init__(
            hass,
            _LOGGER,
            name="Hebrew Events",
            update_interval=timedelta(hours=1),
        )

    async def _async_update_data(self):
        return True