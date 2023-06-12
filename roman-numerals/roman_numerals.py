MAPPING = [
  (1000, 'M'),
  (900, 'CM'),
  (500, 'D'),
  (400, 'CD'),
  (100, 'C'),
  (90, 'XC'),
  (50, 'L'),
  (40, 'XL'),
  (10, 'X'),
  (9, 'IX'),
  (5, 'V'),
  (4, 'IV'),
  (1, 'I')
]


def roman(number: int) -> str:
    if number <= 0:
        return ''
    x, y = next(x for x in MAPPING if x[0] <= number)
    return y + roman(number - x)
