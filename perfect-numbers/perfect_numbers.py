import math


# https://github.com/asarkar/exercism-rust/blob/master/perfect-numbers/src/lib.rs
def classify(num: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if num < 1:
        raise ValueError("Classification is only possible for positive integers.")

    if num == 2:
        return "deficient"

    x = int(math.sqrt(num))
    s = 1
    n = num

    for i in range(2, x + 1):
        curr_term = curr_sum = 1

        while n % i == 0:
            n //= i
            curr_term *= i
            curr_sum += curr_term

        s *= curr_sum

    if n > 2:
        s *= 1 + n

    s -= num

    if s < num:
        return "deficient"
    if s > num:
        return "abundant"
    return "perfect"
