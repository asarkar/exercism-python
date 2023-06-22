import functools
from collections import Counter

# Score categories.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice: list[int], category: int) -> int:
    freq = Counter(dice)
    n = len(freq)
    result = 0

    if category <= 6:
        result = freq[category] * category
    elif category == FULL_HOUSE and n == 2:
        result = functools.reduce(
            lambda acc, x: acc + x[0] * x[1],
            filter(lambda x: x[1] in {2, 3}, freq.items()),
            0
        )
    elif category == FOUR_OF_A_KIND:
        result = functools.reduce(
            lambda _, x: x[0] * 4,
            filter(lambda x: x[1] >= 4, freq.items()),
            0
        )
    elif category == LITTLE_STRAIGHT and n == 5 and 6 not in freq:
        result = 30
    elif category == BIG_STRAIGHT and n == 5 and 1 not in freq:
        result = 30
    elif category == CHOICE:
        result = sum(dice)
    elif category == YACHT and n == 1:
        result = 50

    return result
