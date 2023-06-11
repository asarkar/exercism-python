import re


def translate(text: str) -> str:
    return ' '.join([translate_word(w) for w in text.split()])


VOWELS = 'a|e|i|o|u'
CONSONANTS = f'[^{VOWELS}]'


# https://www.youtube.com/watch?v=6BTwBNmmxzs
def translate_word(word: str) -> str:
    parts = re.split(rf'({VOWELS}|{CONSONANTS}*qu|xr|y)', word)
    parts = [w for w in parts if w]
    if not (
            re.match(rf'^{VOWELS}|xr', parts[0]) or
            (parts[0] == 'y' and re.match(rf'^{CONSONANTS}', parts[1]))
    ):
        fst = parts.pop(0)
        parts.append(fst)

    parts.append('ay')

    return ''.join(parts)
