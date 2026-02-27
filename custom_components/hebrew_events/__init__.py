import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import DOMAIN, STORAGE_KEY, STORAGE_VERSION

PLATFORMS = ["binary_sensor"]

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN]["store"] = Store(hass, STORAGE_VERSION, STORAGE_KEY)
    hass.services.async_register(DOMAIN, "add_event", async_add_event)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True