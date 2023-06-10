import string


def is_pangram(sentence: str) -> bool:
    return set(sentence.lower()) >= set(string.ascii_lowercase)
