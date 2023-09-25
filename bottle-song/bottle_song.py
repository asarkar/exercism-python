WORDS = [
    "No",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
]


def recite(start: int, take: int = 1) -> list[str]:
    rhyme: list[str] = []
    for i in range(start, start - take, -1):
        rhyme.extend(
            [
                f"{WORDS[i]} green {_bottle(i)} hanging on the wall,",
                f"{WORDS[i]} green {_bottle(i)} hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                f"There'll be {WORDS[i - 1].lower()} green {_bottle(i - 1)} hanging on the wall.",
                "",
            ]
        )
    rhyme.pop()
    return rhyme


def _bottle(i: int) -> str:
    return f"bottle{'' if i == 1 else 's'}"
