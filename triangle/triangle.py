def equilateral(sides: list[int]) -> bool:
    a, b, c = sides
    return __is_valid(sides) and (a == b == c)


def isosceles(sides: list[int]) -> bool:
    a, b, c = sides
    return __is_valid(sides) and (a == b or b == c or a == c)


def scalene(sides: list[int]) -> bool:
    return __is_valid(sides) and not equilateral(sides) and not isosceles(sides)


def __is_valid(sides: list[int]) -> bool:
    a, b, c = sides
    non_zero_sides = a > 0 and b > 0 and c > 0
    valid_length_equality = (a + b >= c) and (a + c >= b) and (b + c >= a)
    return non_zero_sides and valid_length_equality
