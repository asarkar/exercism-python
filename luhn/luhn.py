import itertools


# pylint: disable=R0903
class Luhn:
    def __init__(self, card_num: str) -> None:
        self.card_num = card_num

    def valid(self) -> bool:
        def go(n: int, mul: int) -> int:
            return n * mul - (9 if mul == 2 and n > 4 else 0)

        xs = [c for c in self.card_num if c.isdigit() or c.isspace()]
        if len(xs) != len(self.card_num):
            return False
        ys = zip(filter(lambda x: x.isdigit(), reversed(xs)), itertools.cycle([1, 2]))
        zs = [go(int(x), y) for x, y in ys]
        return len(zs) > 1 and (sum(zs) % 10) == 0
