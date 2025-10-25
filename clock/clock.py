from __future__ import annotations


class Clock:
    def __init__(self, hour: int, minute: int) -> None:
        # `//` returns the Euclidean quotient of `a` divided by `b`.
        # It performs floor division, rounding the quotient toward negative infinity.
        # Examples:
        # -40 // -60 =  0
        #  40 // -60 = -1
        # -40 // 60  = -1
        #  40 // 60  =  0
        hour = (hour + (minute // 60)) % 24
        self.hours = hour
        # `%` returns the Euclidean remainder of `a` divided by `b`.
        # The result always has the same sign as the divisor `b`.
        # Examples:
        # -40 % -60 = -40
        #  40 % -60 = -20
        # -40 % 60  =  20
        #  40 % 60  = 40
        self.minutes = minute % 60

    def __repr__(self) -> str:
        return f"Clock({self.hours}, {self.minutes})"

    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Clock) and str(self) == str(other)

    def __add__(self, minutes: int) -> Clock:
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes: int) -> Clock:
        return Clock(self.hours, self.minutes - minutes)
