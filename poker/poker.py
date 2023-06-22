from collections import defaultdict
from enum import Enum, auto


class PokerHand(Enum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()


def best_hands(hands: list[str]) -> list[str]:
    xs = map(lambda x: (x[0], poker_hand(x[1])), enumerate(hands))
    # Sort the hands in desc order based on the enum values, and break tie using the ranks.
    # Since the ranks are also sorted in desc order, [8, 8, 8, 8, 7] > [8, 8, 8, 8, 6].
    poker_hands = sorted(xs, key=lambda x: (x[1][0].value, x[1][1]), reverse=True)
    # The first hand is the best hand.
    fst = (poker_hands[0][1][0].value, poker_hands[0][1][1])
    # There may be multiple winners.
    return [hands[i] for i, x in poker_hands if (x[0].value, x[1]) == fst]


def poker_hand(hand: str) -> tuple[PokerHand, list[int]]:  # noqa: C901, pylint: disable=R0912
    """
    Return a tuple consisting of the poker hand and the sorted ranks in the hand.

    :param hand: hand, like "4S 5S 7H 8D JC"
    :return: a tuple, like (HIGH_CARD, [11, 8, 7, 5, 4])
    """
    rm = rank_map(hand)
    # Sort ranks in desc order by the length of their groups,
    # and for equal-length groups, break tie using the key (rank).
    # A rank group consists of the suites of the same rank.
    sorted_ranks = sorted(map(lambda x: (len(x[1]), x[0]), rm.items()), reverse=True)
    rank_grp_len = [x[0] for x in sorted_ranks]
    ranks = [x[1] for x in sorted_ranks]
    # Count all the unique suites.
    num_suites = len({x for xs in rm.values() for x in xs})
    num_ranks = len(ranks)
    result = None
    if num_ranks == 5:
        five_high = ranks == [14, 5, 4, 3, 2]
        last_rank = ranks[-1]
        # Check if the ranks are sequential.
        seq = five_high or all((last_rank <= r <= last_rank + 4) for r in ranks)
        # There's a test that says a 5-high straight flush
        # is the lowest-scoring straight flush.
        if num_suites == 1 and five_high and seq:
            result = (PokerHand.STRAIGHT_FLUSH, [0, 1, 2, 3, 4])
        elif num_suites == 1 and seq:
            result = (PokerHand.STRAIGHT_FLUSH, ranks)
        elif num_suites == 1:
            result = (PokerHand.FLUSH, ranks)
        # There's a test that says a 5-high straight
        # is the lowest-scoring straight.
        elif seq and num_suites > 1 and five_high:
            result = (PokerHand.STRAIGHT, [0, 1, 2, 3, 4])
        elif seq and num_suites > 1:
            result = (PokerHand.STRAIGHT, ranks)
        else:
            result = (PokerHand.HIGH_CARD, ranks)
    elif num_ranks == 2:
        if rank_grp_len == [4, 1]:
            result = (PokerHand.FOUR_OF_A_KIND, ranks)
        elif rank_grp_len == [3, 2]:
            result = (PokerHand.FULL_HOUSE, ranks)
    elif num_ranks == 3:
        if rank_grp_len == [3, 1, 1]:
            result = (PokerHand.THREE_OF_A_KIND, ranks)
        elif rank_grp_len == [2, 2, 1]:
            result = (PokerHand.TWO_PAIR, ranks)
    elif num_ranks == 4:
        result = (PokerHand.ONE_PAIR, ranks)
    else:
        result = (PokerHand.HIGH_CARD, ranks)

    assert result, f'num_ranks={num_ranks}'
    return result


def rank_map(hand: str) -> dict[int, set[str]]:
    """
    Returns a map of rank: suites.

    :param hand: hand, like "4S 5S 4H 8D JC"
    :return: map, like {4: {'S', 'H'}, 5: {'S'}, 8: {'D'}, 11: {'C'}}
    """
    result: dict[int, set[str]] = defaultdict(set)
    for w in hand.split():
        rank, suite = w[:-1], w[-1]
        if rank == 'A':
            r = 14
        elif rank == 'K':
            r = 13
        elif rank == 'Q':
            r = 12
        elif rank == 'J':
            r = 11
        else:
            r = int(rank)
        result[r].add(suite)

    return result
