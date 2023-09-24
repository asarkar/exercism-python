COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIXES = [(10, "giga"), (7, "mega"), (4, "kilo"), (1, "")]


def label(colors: list[str]) -> str:
    num: float = COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
    if num == 0:
        return "0 ohms"
    num_zeros = COLORS.index(colors[2])
    num_digits = 2 + num_zeros
    num_digits, prefix = next(p for p in PREFIXES if num_digits >= p[0])
    multiplier = pow(10, num_zeros - num_digits + 1)
    num *= multiplier
    return f"{int(num)} {prefix}ohms"
