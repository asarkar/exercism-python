import itertools
import sys


def total(basket: list[int]) -> int:
    freq = [0] * 6
    for b in basket:
        freq[b] += 1
    return __bag_books(freq, {})


COST_OF_ONE = 800
DISCOUNTS = [0, 0, 40, 80, 160, 200]


# For this problem, it only matters how many different types of books are there.
# At each iteration, we either put a book in the same basket, or in a new basket.
# Since we don't know any better, we have to try both options and see which basket
# ends up costing less.
# Instead of operating on the input array, we are going to be working with a
# frequency array. So, [1, 1, 2] becomes [0, 2, 1, 0, 0, 0]. The array is of
# size six for convenience, so, that we can use the books directly as indices
# without having to subtract 1.
#
# 2. A naive caching/memoization approach would use the frequency array directly as
# the key, but note that [0, 1, 2, 0, 0, 0] and [0, 2, 1, 0, 0, 0] cost exactly the
# same. Thus, we use a sorted, non-zero, frequency array as the cache key.
# In the above example, it is [1, 2].
#
# 3. Lastly, note that [1, 1] (zeros removed) will produce three combinations,
# [[1], [1], [1, 1]], of which the first two are identical. Thus, we deduplicate
# the combinations before iterating on them.
def __bag_books(freq: list[int], memo: dict[tuple[int, ...], int]) -> int:
    # freq=[0, 1, 2] and freq=[2, 0, 1] have the same cost.
    key = tuple(sorted(x for x in freq if x > 0))
    if key in memo:
        return memo[key]

    # Remaining books that can be added to the basket.
    remaining = [i for i, x in enumerate(freq) if x > 0]
    if not remaining:
        memo[key] = 0
        return 0

    cost = sys.maxsize
    basket = set()

    def index2count(g: tuple[int, ...]) -> list[int]:
        return [freq[x] for x in g]

    for i in range(1, len(remaining) + 1):
        # Try adding all combinations of the remaining books to the basket.
        xs = sorted(itertools.combinations(remaining, i), key=index2count)
        # Dedup combinations that have the same counts.
        # For example, remaining=[1, 1] has three combinations ((1,), (1,), (1, 1)),
        # where the second combination is redundant.
        choices = itertools.groupby(xs, key=index2count)
        # g is a tuple of i-tuples where each i-tuple indicates the books put
        # in the same basket. For example, ((1,), (1,)) or ((1, 2), (2, 3)),
        # (1, 2) means books 1 and 2 are put in the same basket.
        # Note that the tuple values are indices into the frequency array.
        # Since the tuples in a group are identical, we can pick any.
        for _, g in choices:
            x = next(g)
            for b in x:
                basket.add(b)
                freq[b] -= 1

            n = len(basket)
            cost_of_basket = (COST_OF_ONE - DISCOUNTS[n]) * n
            # Check the cost of the current basket, and start a new basket.
            cost = min(cost, cost_of_basket + __bag_books(freq, memo))

            # Undo the current combination and try another.
            for b in x:
                basket.remove(b)
                freq[b] += 1

    memo[key] = cost
    return cost
