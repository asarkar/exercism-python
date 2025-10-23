import calendar
from dataclasses import dataclass
from datetime import date


@dataclass
class MeetupDayException(ValueError):
    msg: str


INDEX_MAP = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4, "last": -1}


def meetup(year: int, month: int, week: str, day_of_week: str) -> date:
    num_days = calendar.monthrange(year, month)[1]
    all_days = [date(year, month, day) for day in range(1, num_days + 1)]
    days = [d for d in all_days if day_of_week == calendar.day_name[d.weekday()]]

    if week == "teenth":
        return next(d for d in days if 13 <= d.day <= 19)
    if (i := INDEX_MAP[week]) < len(days):
        return days[i]

    raise MeetupDayException("That day does not exist.")
