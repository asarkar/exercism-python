import math


# We use Euclid's formula of generating a tuple.
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#
# a = m^2 - n^2, b = 2mn, c = m^2 + n^2, where m > n > 0 ---(i)
# a + b + c = P ---(ii)
#
# Combining equations (i) and (ii), we have:
# 2m^2 + 2mn = P ---(iii)
#
# Since m > n > 0, 1 <= n <= m - 1.
# Putting n=1 in equation (iii), we have:
# 2m^2 + 2m - P = 0, ax^2 + bx + c = 0, a=2, b=2, c=-P
#  m = (-b +- sqrt(b^2 - 4ac)) / 2a
#  => (-2 +- sqrt(4 + 8P)) / 4
#  => (-1 +- sqrt(1 + 2P)) / 2
#
# Since m > 0, sqrt(b^2 - 4ac) > -b, the only solution is
#  (-1 + sqrt(1 + 2P)) / 2 ---(iv)
#
# Putting n=m-1 in equation (iii), we have:
# 2m^2 + 2m(m - 1) - P = 0
#  => 4m^2 - 2m - P = 0, ax^2 + bx + c = 0, a=4, b=-2, c=-P
#  m = (-b +- sqrt(b^2 - 4ac)) / 2a
#  => (2 +- sqrt(4 + 16P)) / 8
#  => (1 +- sqrt(1 + 4P)) / 4
#
# Since m > 0, the only solution is (1 + sqrt(1 + 4P)) / 4 ---(v)
#
# From equation (iii), m^2 + mn = P/2; since P/2 is constant,
# when n is the smallest, m must be the largest, and vice versa.
#
# Thus, (1 + sqrt(1 + 4P)) / 4 <= m <= (-1 + sqrt(1 + 2P)) / 2 ---(vi)
#
# Solving equation (iii) for n, we have:
#  n = (P - 2m^2) / 2m ---(vii)
#
# We iterate for m within the bounds given by the inequality (vi)
# and check when the corresponding n given by equation (vii) is
# an integer.
#
# Despite generating all primitive triples, Euclid's formula does not
# produce all triples - for example, (9, 12, 15) cannot be generated using
# integer m and n. This can be remedied by inserting an additional
# parameter k to the formula. The following will generate all Pythagorean
# triples uniquely.
# a = k(m^2 - n^2), b = 2kmn, c = k(m^2 + n^2), for k >= 1.
#
# Thus, we iterate for integer values of P/k until P < 12,
# lowest possible perimeter corresponding to the triple (3, 4, 5).
def triplets_with_sum(number: int) -> list[list[int]]:
    triplets: set[frozenset[int]] = set()
    for k in range(1, (number // 12) + 1):
        s = number / k
        if not s.is_integer():
            continue
        min_m = int((1.0 + math.sqrt(1.0 + 4.0 * s)) / 4.0)
        max_m = int((-1.0 + math.sqrt(1.0 + 2.0 * s)) / 2.0)
        for m in range(min_m, max_m + 1):
            numerator = s - 2 * m * m
            if numerator <= 0:
                continue
            n = numerator / (2 * m)
            if m > n and n.is_integer():
                i = int(m)
                j = int(n)
                a = k * (i * i - j * j)
                b = k * 2 * i * j
                c = k * (i * i + j * j)
                triplets.add(frozenset([a, b, c]))

    return sorted([sorted(t) for t in triplets])
