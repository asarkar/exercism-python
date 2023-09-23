from enum import Enum


class Color(Enum):
    BLACK = 0
    BROWN = 1
    RED = 2
    ORANGE = 3
    YELLOW = 4
    GREEN = 5
    BLUE = 6
    VIOLET = 7
    GREY = 8
    WHITE = 9


def color_code(color: str) -> int:
    # next takes an iterator as the first parameter and
    # (x for x in lst if ...) is a generator over the list lst
    # (which is an iterator).
    return next((clr.value for clr in Color if clr.name.lower() == color))


def colors() -> list[str]:
    return [clr.name.lower() for clr in Color]
