import string
from collections import Counter


def is_isogram(text: str) -> bool:
    alpha = set(string.ascii_lowercase)
    for letter, count in Counter(text.lower()).items():
        if letter in alpha and count > 1:
            return False
    return True
