from typing import TypeAlias

Array: TypeAlias = list["ArrayValue"]
ArrayValue: TypeAlias = int | None | Array


def flatten(iterable: Array) -> list[int]:
    result: list[int] = []
    for i in iterable:
        if isinstance(i, list):
            result.extend(flatten(i))
        elif i is not None:
            result.append(i)

    return result
