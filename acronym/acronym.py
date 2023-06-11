def abbreviate(words: str) -> str:
    xs = []
    for i, ch in enumerate(words):
        prev = '' if i == 0 else words[i - 1]
        fst = ch.isalpha() and (i == 0 or prev.isspace() or prev == '-')
        if fst or (ch.isupper() and not prev.isupper()):
            xs.append(ch.upper())

    return ''.join(xs)
