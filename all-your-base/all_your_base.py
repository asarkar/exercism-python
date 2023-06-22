# 1. Convert to decimal using Horner's method (https://en.wikipedia.org/wiki/Horner%27s_method).
# 2. Convert to the target base.
def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    dec = __decimal(input_base, digits)
    if dec == 0:
        return [0]
    result = []
    while dec > 0:
        dec, x = divmod(dec, output_base)
        result.append(x)
    return result[::-1]


def __decimal(base: int, digits: list[int]) -> int:
    if not digits:
        return 0
    x = digits.pop()
    if x < 0 or x >= base:
        raise ValueError('all digits must satisfy 0 <= d < input base')
    return x + base * __decimal(base, digits)
