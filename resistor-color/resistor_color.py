from enum import Enum

Color = Enum('Color', ['BLACK', 'BROWN', 'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'VIOLET', 'GREY', 'WHITE'])


def color_code(color: str) -> int:
    # next takes an iterator as the first parameter and
    # (x for x in lst if ...) is a generator over the list lst
    # (which is an iterator).
    return next((clr.value - 1 for clr in Color if clr.name.lower() == color))


def colors() -> list[str]:
    return [clr.name.lower() for clr in Color]
