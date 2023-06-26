NUM_LETTERS = 26


def rotate(text: str, key: int) -> str:
    k = (key % NUM_LETTERS) + (NUM_LETTERS if key < 0 else 0)
    return "".join([chr(__shift(k, ch)) for ch in text])


def __shift(key: int, ch: str) -> int:
    x = key + ord(ch)
    if ch.isupper() and x > ord("Z"):
        return x - NUM_LETTERS
    if ch.lower() and x > ord("z"):
        return x - NUM_LETTERS
    if ch.isalpha():
        return x
    return ord(ch)
