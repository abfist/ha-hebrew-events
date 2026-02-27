from homeassistant import config_entries
import voluptuous as vol

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
            vol.Required("name"): str,
            vol.Required("type"): vol.In(["yahrzeit", "birthday"]),
            vol.Required("day"): vol.All(int, vol.Range(min=1, max=30)),
            vol.Required("month"): vol.All(int, vol.Range(min=1, max=13)),
            vol.Optional("adar_type", default="auto"):
                vol.In(["auto", "adar1", "adar2"]),
            vol.Optional("reminders", default=""): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema
        )