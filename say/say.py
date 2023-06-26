MAPPING = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

ZEROS = [
    (1_000_000_000_000, "trillion"),
    (1_000_000_000, "billion"),
    (1_000_000, "million"),
    (1_000, "thousand"),
    (100, "hundred"),
]


def say(number: int) -> str:
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    return __say(number) if number else "zero"


def __say(number: int) -> str:
    if number in MAPPING:
        return MAPPING[number]

    # Find the number with the greatest number of zeros
    # less than or equal to n.
    # Example: For 120, this will find 100.
    closest = next((x for x in ZEROS if x[0] <= number), None)
    if closest:
        x, y = closest
        left, right = divmod(number, x)
        return " ".join([__say(left), y, __say(right)]).strip()

    # n < 100
    left, right = divmod(number, 10)
    return f"{MAPPING[left * 10]}-{MAPPING[right]}"
