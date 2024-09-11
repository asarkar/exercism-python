import itertools
import sys
from collections import Counter


def total(books: list[int]) -> int:
    freq = tuple(x for _, x in Counter(books).most_common())
    return _bag_books(freq, {})


COST_OF_ONE = 800
DISCOUNTS = [0, 0, 40, 80, 160, 200]


# For this problem, it only matters how many different types of books are there.
# At each iteration, we either put a book in the same basket, or in a new basket.
# Since we don't know any better, we have to try both options and see which basket
# ends up costing less.
# Instead of operating on the input array which may be large, we are going to be
# working with a frequency array which is limited to size 5.
#
# A naive caching/memoization approach would use the frequency array directly as
# the key, but note that [1, 2] and [2, 1, 0] cost exactly the same.
# Thus, we use a sorted, positives only, frequency array as the cache key.
# In the above example, it is [1, 2].
def _bag_books(freq: tuple[int, ...], memo: dict[tuple[int, ...], int]) -> int:
    if freq in memo:
        return memo[freq]

    # Different books that can be added to the basket are
    # represented by the indices of the frequency array.
    remaining = list(range(len(freq)))
    if not remaining:
        memo[freq] = 0
        return 0

    cost = sys.maxsize

    for i in range(1, len(remaining) + 1):
        for basket in itertools.combinations(remaining, i):
            # fmt: off
            # Decrement frequencies for the books in the basket
            # and remove zero entries.
            new_freq = [x - bool(j in basket) for j, x
                        in enumerate(freq)
                        if j not in basket or x > 1]
            # fmt: on
            new_freq.sort(reverse=True)
            n = len(basket)
            cost_of_basket = (COST_OF_ONE - DISCOUNTS[n]) * n
            # Check the cost of the current basket, and start a new basket.
            cost = min(cost, cost_of_basket + _bag_books(tuple(new_freq), memo))

    memo[freq] = cost
    return cost
