import itertools
import operator
import random
import string
from typing import Callable


class Cipher:
    def __init__(self, key: str = None) -> None:
        if key:
            self.key = key
        else:
            self.key = "".join(random.choices(string.ascii_lowercase, k=101))

    def encode(self, text: str) -> str:
        return self.__xcode(text, operator.add)

    def decode(self, text: str) -> str:
        return self.__xcode(text, operator.sub)

    def __xcode(self, text: str, fn: Callable[[int, int], int]) -> str:
        key = itertools.cycle(self.key)
        xs = zip(key, text)
        return "".join([Cipher.__go(x, y, fn) for x, y in xs])

    @staticmethod
    def __go(x: str, y: str, fn: Callable[[int, int], int]) -> str:
        a = ord("a")
        offset = ord(x) - a
        c = fn(ord(y) - a, offset) % 26
        return chr(c + a)
