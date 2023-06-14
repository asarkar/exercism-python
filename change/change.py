import sys


def find_fewest_coins(denominations: list[int], amount: int) -> list[int]:
    if amount < 0:
        raise ValueError("target can't be negative")
    if amount == 0:
        return []
    coins = make_change(denominations, amount)
    if coins[amount] < 0:
        raise ValueError("can't make target with given coins")
    change = []
    while amount > 0:
        coin = denominations[coins[amount]]
        change.append(coin)
        amount -= coin

    return sorted(change)


def make_change(denominations: list[int], amount: int) -> list[int]:
    """
    Change making algorithm from
    http://www.ccs.neu.edu/home/jaa/CSG713.04F/Information/Handouts/dyn_prog.pdf

    This function uses two arrays:

    min_coins: min_coins[i] is the minimum number of coins needed
    to make change for amount 'i'.  It is only used internally.

    coins: the _first_ coin used to make change for amount n
    (actually stores the coin _index_ into the coins array).
    """

    # min_coins[0] = 0, because no coins are needed to make change
    # for zero amount.
    min_coins = [0] + [sys.maxsize] * amount
    coins = [-1] * (amount + 1)

    for amt in range(1, 1 + amount):
        # Fewest coins needed to make 'amt'.
        min_coin = sys.maxsize
        for i, denom in enumerate(denominations):
            # Take this denomination only if it can make 'amt' in fewer
            # coins than we have so far.
            if denom <= amt and (x := 1 + min_coins[amt - denom]) < min_coin:
                min_coin = x
                coins[amt] = i
        min_coins[amt] = min_coin

    return coins
