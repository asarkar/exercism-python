"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 0
UNEQUAL = 2


def sublist(list_one: list[int], list_two: list[int]) -> int:
    x, y = len(list_one), len(list_two)
    smaller = list_one if x <= y else list_two
    larger = list_one if x > y else list_two
    n = len(smaller)
    for i in range(len(larger) - n + 1):
        if smaller == larger[i: n + i]:
            if x < y:
                return SUBLIST
            if x > y:
                return SUPERLIST
            return EQUAL
    return UNEQUAL
