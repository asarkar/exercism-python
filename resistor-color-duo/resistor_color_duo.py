from enum import Enum

Color = Enum('Color', ['BLACK', 'BROWN', 'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'VIOLET', 'GREY', 'WHITE'])


def value(colors: list[str]) -> int:
    codes = [str(__color_code(clr)) for clr in colors[:2]]
    return int(''.join(codes))


def __color_code(color: str) -> int:
    # next takes an iterator as the first parameter and
    # (x for x in lst if ...) is a generator over the list lst
    # (which is an iterator).
    return next((clr.value - 1 for clr in Color if clr.name.lower() == color))
