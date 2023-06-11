import heapq


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    q = []
    for i in multiples:
        if i > 0:
            heapq.heappush(q, (i, i))

    s = prev = 0
    while q:
        x, y = heapq.heappop(q)
        if (x < limit) and (x != prev):
            prev = x
            s += x
        elif x >= limit:
            break

        if (x + y) < limit:
            heapq.heappush(q, (x + y, y))

    return s
