from collections import defaultdict
from typing import Optional

Domino = tuple[int, int]


class FaceValueMap:
    def __init__(self, dominoes: list[Domino]):
        self.map: dict[int, set[int]] = defaultdict(set)
        self.dominoes = dominoes
        for i in range(len(dominoes)):
            self.release(i)

    def acquire(self, i: int) -> None:
        l, r = self.dominoes[i]  # noqa: E741
        self.map[l].remove(i)
        # If l = r, then 'i' is no longer in the set
        self.map[r].discard(i)

    def release(self, i: int) -> None:
        l, r = self.dominoes[i]  # noqa: E741
        self.map[l].add(i)
        self.map[r].add(i)

    # 1. Should return all indices that have either left
    #    or right matching the given domino side.
    # 2. Should not contain the given domino.
    # 3. Should not contain duplicate indices.
    # 4. Should contain identical dominoes with unique indices.
    def candidates(self, i: int, left: bool) -> list[int]:
        l, r = self.dominoes[i]  # noqa: E741
        side = l if left else r
        return [x for x in self.map[side] if x != i]


# The problem can be rephrased to say that given some pairs/tuples,
# arrange them such that the adjacent sides have the same number.
#
# You might think that given [(1, 1), (2, 2)], a possible answer is
# [(1, 2), (2, 1)], but no, because the pairs (1, 2) and (2, 1)
# don't exist in the input. However, given [(1, 2) and (1, 2)],
# [(1, 2), (2, 1)] is acceptable because we simply flipped the
# tuple (2, 1).
#
# Thus, the problem reduces to finding tuples with either the left
# or the right matching a given number, and trying them one by one
# until a complete chain of dominoes is formed.
#
# We keep a Map of left and right values as the keys, and the
# corresponding domino indices as the values. According to the usual
# backtracking paradigm, we need to acquire and release an index,
# so we provide methods to do so.
def can_chain(dominoes: list[Domino]) -> Optional[list[Domino]]:
    result: list[Domino] = []
    fvm = FaceValueMap(dominoes)

    def solve(left: bool, i: int) -> bool:
        """
        :param left: true indicates candidates should be
        matched by their left face values
        :param i: index of the domino
        :return: true if chaining is feasible, false otherwise
        """
        l, r = dominoes[i]  # noqa: E741
        # Since we append new dominoes at the end,
        # if matched on the left side, a domino has
        # to be flipped.
        result.append((r, l) if left else (l, r))
        fvm.acquire(i)
        for j in fvm.candidates(i, left):
            x = dominoes[j][1]
            # If dominoes[j] is matched on the right side,
            # then its candidates should be matched on
            # their left.
            if solve(x in {l, r}, j):
                return True

        fvm.release(i)
        if len(result) == len(dominoes):
            return result[0][0] == result[-1][1]

        result.pop()
        return False

    if not dominoes:
        return []
    # Due to the symmetry in the problem, it doesn't matter which
    # domino or side we start from.
    return result if solve(False, 0) else None
