import heapq


def prime(number: int) -> int:
    if number <= 0:
        raise ValueError("there is no zeroth prime")
    count = 0
    i = 2
    p = 0
    composites: list[tuple[int, int]] = []

    # Sieve of Eratosthenes.
    while count < number:
        if not composites or composites[0][0] != i:
            p = i
            count += 1
            x = i * i
            heapq.heappush(composites, (x, i))
        else:
            while composites and composites[0][0] == i:
                x, y = heapq.heappop(composites)
                heapq.heappush(composites, (x + y, y))

        i += 1

    return p
