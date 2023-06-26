def score(word: str) -> int:
    return sum(__score(ch.upper()) for ch in word)


def __score(letter: str) -> int:
    result = 0
    if letter in {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"}:
        result = 1
    elif letter in {"D", "G"}:
        result = 2
    elif letter in {"B", "C", "M", "P"}:
        result = 3
    elif letter in {"F", "H", "V", "W", "Y"}:
        result = 4
    elif letter == "K":
        result = 5
    elif letter in {"J", "X"}:
        result = 8
    elif letter in {"Q", "Z"}:
        result = 10

    return result
