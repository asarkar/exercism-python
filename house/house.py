PARAGRAPH = [
    "This is the horse and the hound and the horn",
    "that belonged to the farmer sowing his corn",
    "that kept the rooster that crowed in the morn",
    "that woke the priest all shaven and shorn",
    "that married the man all tattered and torn",
    "that kissed the maiden all forlorn",
    "that milked the cow with the crumpled horn",
    "that tossed the dog",
    "that worried the cat",
    "that killed the rat",
    "that ate the malt",
    "that lay in the house that Jack built.",
]


# The pattern is that for a given line number n, it contains the last n lines
# of the paragraph. The first of these lines should start with "This is the",
# so, we split the line around the word "the", and prepend "This is" to the
# segment to the right of "the".
# We then concatenate the n lines using whitespace.
def recite(start_verse: int, end_verse: int) -> list[str]:
    rhyme: list[str] = []
    for line_number in range(start_verse, end_verse + 1):
        if line_number == 12:
            rhyme.append(" ".join(PARAGRAPH))
        else:
            lines = PARAGRAPH[-line_number:]
            i = lines[0].index("the")
            lines[0] = f"This is {lines[0][i:]}"
            rhyme.append(" ".join(lines))
    return rhyme
