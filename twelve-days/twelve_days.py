PARAGRAPH = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "and a Partridge in a Pear Tree.",
]

WORDS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]


def recite(start_verse: int, end_verse: int) -> list[str]:
    rhyme: list[str] = []
    for line_number in range(start_verse, end_verse + 1):
        lines = [f"On the {WORDS[line_number - 1]} day of Christmas my true love gave to me: "]
        if line_number == 1:
            lines.append("a Partridge in a Pear Tree.")
        else:
            lines.extend(PARAGRAPH[-line_number:])
        rhyme.append("".join(lines))
    return rhyme
