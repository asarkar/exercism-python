def is_valid(isbn: str) -> bool:
    s = 0
    i = 10
    for ch in isbn:
        if ch.isdigit():
            s += int(ch) * i
            i -= 1
        elif ch == "X" and i == 1:
            s += 10
            i -= 1
        elif ch != "-":
            return False

    return s % 11 == 0 and i == 0
