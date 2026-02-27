from pyluach import dates
from datetime import date, timedelta

def resolve_month(year, month, adar_type):
    if month != 12:
        return month

    if not dates.HebrewDate(year, 1, 1).leap:
        return 12

    if adar_type == "adar1":
        return 12
    if adar_type == "adar2":
        return 13

    return 13  # ברירת מחדל באוטומטי

def next_occurrence(day, month, adar_type="auto"):
    today = dates.HebrewDate.today()
    year = today.year

    resolved_month = resolve_month(year, month, adar_type)
    target = dates.HebrewDate(year, resolved_month, day)

    if target.to_greg().date() < date.today():
        year += 1
        resolved_month = resolve_month(year, month, adar_type)
        target = dates.HebrewDate(year, resolved_month, day)

    return target.to_greg().date()