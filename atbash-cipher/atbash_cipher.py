def encode(plain_text: str) -> str:
    cipher = __xcode(plain_text)
    return ' '.join(__chunks(cipher, 5))


def __chunks(text: str, n: int) -> list[str]:
    return [text[i:i + n] for i in range(0, len(text), n)]


def decode(ciphered_text: str) -> str:
    return __xcode(ciphered_text)


def __xcode(text: str) -> str:
    xs = []
    for ch in text.lower():
        if ch.islower():
            x = chr(ord('a') + (ord('z') - ord(ch)))
            xs.append(x)
        elif ch.isdigit():
            xs.append(ch)
    return ''.join(xs)
