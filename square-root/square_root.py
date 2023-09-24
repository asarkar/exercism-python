def square_root(n: int) -> int:
    r = float(n)
    precision = 10 ** (-6)

    while abs(n - r * r) > precision:
        r = (r + n / r) / 2

    return int(r)
