import operator
from typing import Callable


def largest(min_factor: int, max_factor: int) -> tuple[int | None, list[list[int]]]:
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return _palindrome(range(max_factor, min_factor - 1, -1), operator.ge)


def smallest(min_factor: int, max_factor: int) -> tuple[int | None, list[list[int]]]:
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    return _palindrome(range(min_factor, max_factor + 1), operator.le)


def _palindrome(r: range, op: Callable[[int, int], bool]) -> tuple[int | None, list[list[int]]]:
    """
    Searches for a palindrome with factors in the given range. Whether the palindrome is the
    maximum or minimum depends on the given operator.

    :param r: range for factors
    :param op: comparison operator, one of '>=' and '<='
    :return: palindrome and it's factors, if found
    """
    if len(r) == 0:
        raise ValueError("min must be <= max")
    palindrome: int | None = None
    factors: list[list[int]] = []

    for left in r:
        # This variable determines whether the last iterations of the inner loop
        # produced a product that satisfied the given condition when compared with
        # the palindrome found so far. Since the ranges are monotonically
        # increasing/decreasing, if no such product was found in the last iteration,
        # it won't be found in any future iterations either, so, we can stop.
        should_continue = False
        # One factor is smaller or equal to the other.
        for right in range(r.start, left + r.step, r.step):
            pdt = left * right
            if palindrome is not None and not op(pdt, palindrome):
                break
            should_continue = True
            x = str(pdt)
            if x != x[::-1]:
                continue
            # If newly found palindrome is not the same as the one found before,
            # we need to reset the factors. One palindrome may have multiple
            # factors, like 9 has [1, 9] and [3, 3].
            if palindrome != pdt:
                factors = []
            palindrome = pdt
            factors.append([left, right])
        if not should_continue:
            break

    return palindrome, factors
