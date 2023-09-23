from __future__ import annotations


class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        hr = hour % 24
        (h, m) = divmod(minute, 60)
        x = (hr + h) % 24
        self.hour = Clock.__normalize(x, 24)
        self.minutes = Clock.__normalize(m, 60)
        self.hr = hour
        self.min = minute

    @staticmethod
    def __normalize(x: int, base: int) -> int:
        return (base - x) if x < 0 else x

    def __repr__(self) -> str:
        return f"Clock({self.hr}, {self.min})"

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minutes:02}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Clock) and str(self) == str(other)

    def __add__(self, minutes: int) -> Clock:
        return Clock(self.hour, self.minutes + minutes)

    def __sub__(self, minutes: int) -> Clock:
        return self.__add__(-minutes)
