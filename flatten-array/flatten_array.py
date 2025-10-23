type Array = list["ArrayValue"]
type ArrayValue = int | None | Array


def flatten(iterable: Array) -> list[int]:
    result: list[int] = []
    for i in iterable:
        if isinstance(i, list):
            result.extend(flatten(i))
        elif i is not None:
            result.append(i)

    return result
