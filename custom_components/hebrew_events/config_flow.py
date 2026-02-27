import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class HebrewEventsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input["name"],
                data=user_input
            )

        schema = vol.Schema({
            vol.Required("type"): vol.In(["yahrzeit", "birthday","holy-day","other"]),
            vol.Required("name"): str,
            vol.Required("day"): int,
            vol.Required("month"): int,
            vol.Optional("reminders", default=""): str
        })

        return self.async_show_form(step_id="user", data_schema=schema)