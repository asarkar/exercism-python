from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    w = word.upper()
    freq = Counter(w)
    # >= Python 3.8
    return [c for c in candidates if (x := c.upper()) != w and Counter(x) == freq]
