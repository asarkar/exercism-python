def encode(plain_text: str) -> str:
    cipher = xcode(plain_text)
    chunk_size = 5
    return ' '.join([cipher[i:i + chunk_size] for i in range(0, len(cipher), chunk_size)])


def decode(ciphered_text: str) -> str:
    return xcode(ciphered_text)


def xcode(text: str) -> str:
    xs = []
    for ch in text.lower():
        if ch.islower():
            x = chr(ord('a') + (ord('z') - ord(ch)))
            xs.append(x)
        elif ch.isdigit():
            xs.append(ch)
    return ''.join(xs)
