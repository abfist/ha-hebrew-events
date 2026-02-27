from datetime import date, timedelta
from homeassistant.components.binary_sensor import BinarySensorEntity
from .manager import next_occurrence
from .const import DOMAIN

sun = hass.states.get("sun.sun")
after_sunset = sun and sun.state == "below_horizon"

def hebrew_today(after_sunset):
    today = dates.HebrewDate.today()
    if after_sunset:
        return today + 1
    return today

async def async_setup_entry(hass, entry, async_add_entities):

    storage = hass.data[DOMAIN]["storage"]
    entities = []

    for card in storage.data:
        entities.append(EventToday(card))
        for r in card["reminders"]:
            entities.append(EventReminder(card, r))

    async_add_entities(entities)


class EventToday(BinarySensorEntity):

    def __init__(self, card):
        self.card = card
        self._attr_name = f"{card['name']} Today"
        self._attr_unique_id = f"{card['id']}_today"

    @property
    def is_on(self):
        return date.today() == next_occurrence(self.card["day"], self.card["month"])


class EventReminder(BinarySensorEntity):

    def __init__(self, card, days_before):
        self.card = card
        self.days_before = days_before
        self._attr_name = f"{card['name']} Reminder {days_before}"
        self._attr_unique_id = f"{card['id']}_reminder_{days_before}"

    @property
    def is_on(self):
        event_date = next_occurrence(self.card["day"], self.card["month"])
        return date.today() == (event_date - timedelta(days=self.days_before))