def leap_year(year: int) -> bool:
    divisible_by_4 = year % 4 == 0
    divisible_by_400 = year % 400 == 0
    divisible_by_100 = year % 100 == 0

    return divisible_by_400 or (divisible_by_4 and not divisible_by_100)
