import math
from collections.abc import Iterator


class Prime:
    def __init__(self) -> None:
        self._values = [1]

    # A good way to speed up this method is to pre-compute and store a list of
    # all primes up to a certain bound, such as all primes up to 200.
    # Such a list can be computed with the Sieve of Eratosthenes.
    # But it's only useful if the prime generator is reused, which, for the tests,
    # isn't the case, so, we don't bother.
    def _is_prime(self, n: int) -> bool:
        # Suppose xy = n = √n * √n. If x ≥ √n, then y ≤ √n and vice-versa.
        # Thus, if xy = n, then one of x or y must be less than or equal to √n.
        # This means that if n can be factored, one of the factors must be less
        # than or equal to √n, so, we only need to check till √n.
        x = int(math.sqrt(n))
        i = 1
        while i < len(self._values) and (y := self._values[i]) <= x:
            if n % y == 0:
                return False
            i += 1
        return True

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        n = self._values[-1] + 1
        while not self._is_prime(n):
            n += 1
        self._values.append(n)
        return n


def factors(value: int) -> list[int]:
    p = Prime()
    ans: list[int] = []
    for i in p:
        while value > 1 and value % i == 0:
            ans.append(i)
            value //= i
        if value <= 1:
            break
    return ans
