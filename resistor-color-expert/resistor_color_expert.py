COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOLERANCES = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}
PREFIXES = [(10, "giga"), (7, "mega"), (4, "kilo"), (1, "")]


def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1:
        return "0 ohms"
    tolerance = TOLERANCES[colors[-1]]
    num_zeros = COLORS.index(colors[-2])
    # Total number of digits after decoding.
    num_digits = len(colors) - 2 + num_zeros
    num_digits, prefix = next(p for p in PREFIXES if num_digits >= p[0])
    num = 0.0
    for clr in colors[:-2]:
        num = num * 10 + COLORS.index(clr)
    multiplier = pow(10, num_zeros - num_digits + 1)
    num *= multiplier
    s = _fmt(num)
    return f"{s} {prefix}ohms ±{tolerance}%"


def _fmt(num: float) -> str:
    s = list(f"{num:.2f}")
    while s and s[-1] == "0":
        s.pop()
    if s and s[-1] == ".":
        s.pop()
    return "".join(s)
