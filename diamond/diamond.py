def rows(letter: str) -> list[str]:
    height = ord(letter) - ord('A') + 1
    top = [__row(height, h) for h in range(height)]
    return top + top[::-1][1:]


def __row(n: int, i: int) -> str:
    ch = chr(ord('A') + i)
    k = n - i - 1
    half = ''.join(ch if x == k else ' ' for x in range(n))
    return half + half[::-1][1:]
