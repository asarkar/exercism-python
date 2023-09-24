import re
from collections import defaultdict


def count_words(sentence: str) -> dict[str, int]:
    pattern = r"\d+|([a-zA-Z]+(?:'??[a-zA-Z]+))|[a-zA-Z]+"
    freq: dict[str, int] = defaultdict(int)
    for m in re.finditer(pattern, sentence):
        freq[m.group(0).lower()] += 1
    return freq
