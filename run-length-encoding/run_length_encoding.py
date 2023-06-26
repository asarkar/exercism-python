import itertools
from typing import Iterator


def decode(string: str) -> str:
    if not string:
        return ""
    count = "".join(itertools.takewhile(lambda x: x.isdigit(), string))
    n = len(count)
    if count:
        i = int(count)
        s = "".join(itertools.repeat(string[n], i))
    else:
        s = string[0]

    return s + decode(string[n + 1 :])


def encode(string: str) -> str:
    def go(it: tuple[str, Iterator[str]]) -> str:
        xs = list(it[1])
        k = len(xs)
        x = k if k > 1 else ""
        return f"{x}{it[0]}"

    return "".join([go(x) for x in itertools.groupby(string)])
