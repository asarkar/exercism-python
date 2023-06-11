def flatten(iterable) -> list[int]:
    result = []
    for i in iterable:
        if isinstance(i, list):
            result.extend(flatten(i))
        elif i is not None:
            result.append(i)

    return result
