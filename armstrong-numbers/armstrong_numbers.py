def is_armstrong_number(number: int) -> bool:
    x = str(number)
    n = len(x)
    s = 0
    for c in x:
        s += int(c) ** n

    return s == number
