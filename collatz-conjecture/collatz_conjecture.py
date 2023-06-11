def steps(number: int) -> int:
    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    u_max = (2 ** 64 - 2) // 3
    x = number
    count = 0

    while x > 1:
        if x % 2 == 0:
            x //= 2
        elif x <= u_max:
            x = 3 * x + 1
        else:
            break
        count += 1

    if x == 1:
        return count
    raise ValueError('Collatz conjecture is disproved!')
