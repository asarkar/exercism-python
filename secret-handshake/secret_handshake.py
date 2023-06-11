def commands(binary_str: str) -> list[str]:
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    hs = [a for (i, a) in zip(range(-1, -5, -1), actions) if binary_str[i] == '1']
    if binary_str[-5] == '1':
        return hs[::-1]
    return hs
