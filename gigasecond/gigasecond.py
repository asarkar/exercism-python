from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    return moment + timedelta(0, 10**9)
