def rows(n: int) -> list[list[int]]:
    if n < 0:
        raise ValueError("number of rows is negative")
    if n == 0:
        return []
    triangle = rows(n - 1)
    triangle.append(__row(n - 1))
    return triangle


# Identity: C(n,k+1) = C(n,k) * (n-k) / (k+1), where n starts from 0.
# We start with C(n,0) = 1, and calculate the rest using the identity.
# But wait...each row is mirrored around the middle element, so,
# we only need to calculate up to the middle element. Then we
# flip the row and append to itself.
def __row(n: int) -> list[int]:
    mid = n // 2
    left = [1]
    x = 1
    for i in range(mid):
        a = n - i
        b = i + 1
        x = (x * a) // b
        left.append(x)

    j = mid + (n % 2)
    right = left[:j]
    right.reverse()
    return left + right
