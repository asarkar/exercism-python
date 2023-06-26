from typing import Callable

M = 26


def encode(plain_text: str, a: int, b: int) -> str:
    if not __mmi(a, M):
        raise ValueError("a and m must be coprime.")

    result = []
    i = 0
    for ch in plain_text:
        if c := __xcode(ch.lower(), lambda x: (a * x + b) % M):
            if i > 0 and (i % 5) == 0:
                result.append(" ")
            result.append(c)
            i += 1

    return "".join(result)


def decode(ciphered_text: str, a: int, b: int) -> str:
    m = __mmi(a, M)
    if not m:
        raise ValueError("a and m must be coprime.")
    result = []
    for ch in ciphered_text:
        if c := __xcode(ch, lambda x: ((x - b) * m) % M):
            result.append(c)

    return "".join(result)


def __xcode(ch: str, fn: Callable[[int], int]) -> str | None:
    if ch.islower():
        x = ord(ch) - ord("a")
        i = fn(x)
        if i < 0:
            i += M
        return chr(i + ord("a"))
    if ch.isdigit():
        return ch
    return None


# MMI of a mod b is a number x such that ax % b = 1.
# We use Extended Euclidean algorithm to find the MMI
# (https://www.youtube.com/watch?v=Gu7iKt2SZYc).
#
# Say a is the larger of the two numbers. Then we can write a = bx + rem. This is known
# as Division Theorem.
# Then, we recurse using b and rem, given rem < b.
# If ever b (smaller) = 0, then the two numbers are not coprimes, and there is no MMI.
# Else if b = 1, the two numbers are coprimes, and a MMI exists.
#  *
# Example: Find the MMI of 17 mod 43.
#  43 = 17x2 + 9
#  17 = 9x1 + 8
#   9 = 8x1 + 1
#
# Since b = 1, we stop, and do "back substitution", i.e. at each step substitute b with
# the equation above.
#  *
# 1 = 9x1 - 8x1
#   = 9x1 - (17x1 - 9x1)
#      = 9x1 - 17x1 + 9x1
#      = -17x1 + 9x2
#   = -17x1 + (43x1 - 17x2)x2
#      = 43x2 -17x5
#
# If a is larger, 2 is the answer, else -5. In our example, a is smaller.
# Since the answer is negative, we add it with the larger, thus 43 - 5 = 38.
# Check (17(a) x 38(MMI)) % 43(b) = 1.
def __mmi(a: int, b: int) -> int | None:
    smaller = min(a, b)
    larger = max(a, b)
    m = __mmi_rec(larger, smaller)
    if not m:
        return None
    x, y = m
    i = y if a == smaller else x
    if i < 0:
        i += larger
    assert (a * i) % b == 1, f"failed check (a->{a} * {i}<-mmi) % {b}<-b == 1"
    return i


def __mmi_rec(larger: int, smaller: int) -> tuple[int, int] | None:
    if smaller == 0:
        return None
    x, y = divmod(larger, smaller)
    if y == 1:
        return y, -x
    m = __mmi_rec(smaller, y)
    return (m[1], -m[1] * x + m[0]) if m else None
