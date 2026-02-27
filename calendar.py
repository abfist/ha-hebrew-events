from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from datetime import datetime
from .manager import next_occurrence
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):

    storage = hass.data[DOMAIN]["storage"]
    async_add_entities([HebrewEventsCalendar(storage)])


class HebrewEventsCalendar(CalendarEntity):

    def __init__(self, storage):
        self.storage = storage
        self._attr_name = "Hebrew Events Calendar"

    async def async_get_events(self, hass, start_date, end_date):
        events = []

        for card in self.storage.data:
            event_date = next_occurrence(card["day"], card["month"])

            if start_date.date() <= event_date <= end_date.date():
                events.append(
                    CalendarEvent(
                        summary=card["name"],
                        start=datetime.combine(event_date, datetime.min.time()),
                        end=datetime.combine(event_date, datetime.min.time())
                    )
                )

        for r in card["reminders"]:
            reminder_date = event_date - timedelta(days=r)
            events.append(
                CalendarEvent(
                    summary=f"{card['name']} (תזכורת {r} ימים)",
                    start=datetime.combine(reminder_date, datetime.min.time()),
                    end=datetime.combine(reminder_date, datetime.min.time())
        )
    )
        return events
    
    