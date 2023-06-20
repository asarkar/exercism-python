import itertools


def drinks_water() -> str:
    resident = __zebra_puzzle()[0]
    assert resident == 1, 'Norwegian drinks water'
    return 'Norwegian'


def owns_zebra() -> str:
    resident = __zebra_puzzle()[1]
    assert resident == 5, 'Japanese owns the Zebra'
    return 'Japanese'


# https://www.youtube.com/watch?v=Qd84SEf6GbM&list=PLAwxTw4SYaPnJVtPvZZ5zXj_wRBjH0FxX&index=77
def __zebra_puzzle() -> (int, int):
    orderings = list(itertools.permutations(range(1, 6)))  # 120 permutations
    first, middle = 1, 3
    # For ints, == and 'is' are the same.
    # We use a generator expression to avoid nested loops,
    # and also to exit early if a solution is found.
    return next((water, zebra)
                for (red, green, ivory, yellow, blue) in orderings
                if __is_immediate_left(ivory, green)    # rule 6
                for (englishman, spaniard, ukrainian, norwegian, japanese) in orderings
                if englishman is red                    # rule 2
                if norwegian is first                   # rule 10
                if __is_next_to(norwegian, blue)        # rule 15
                for (tea, coffee, milk, orange_juice, water) in orderings
                if coffee is green                      # rule 4
                if ukrainian is tea                     # rule 5
                if milk is middle                       # rule 9
                for (dog, fox, horse, snails, zebra) in orderings
                if spaniard is dog                      # rule 3
                for (old_gold, kools, chesterfields, lucky_strike, parliaments) in orderings
                if old_gold is snails                   # rule 7
                if kools is yellow                      # rule 8
                if __is_next_to(chesterfields, fox)     # rule 11
                if __is_next_to(kools, horse)           # rule 12
                if lucky_strike is orange_juice         # rule 13
                if japanese is parliaments              # rule 14
                )


def __is_immediate_left(x: int, y: int) -> bool:
    """
    Checks if x is on the immediate left of y
    """
    return x - y == -1


def __is_next_to(x: int, y: int) -> bool:
    """
    Checks if x is next to y, i.e. on the immediate left or right
    """
    return abs(x - y) == 1
