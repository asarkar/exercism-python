def square_of_sum(n: int) -> int:
    s = n * (n + 1) // 2
    return s * s


# // https://helloacm.com/the-difference-between-sum-of-squares-and-square-of-the-sum/
def sum_of_squares(n: int) -> int:
    return (2 * n + 1) * (n + 1) * n // 6


def difference_of_squares(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)
