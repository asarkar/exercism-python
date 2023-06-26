import math


def cipher_text(plain_text: str) -> str:
    text = __normalize(plain_text)
    if not text:
        return ""
    col = math.ceil(math.sqrt(len(text)))
    chunks = __chunks(text, col)
    cipher = zip(*chunks)
    return " ".join("".join(x) for x in cipher)


def __normalize(text: str) -> str:
    return "".join([c.lower() for c in text if c.isalnum()])


def __chunks(text: str, n: int) -> list[str]:
    return [text[i : i + n].ljust(n) for i in range(0, len(text), n)]
