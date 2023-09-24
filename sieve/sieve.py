import heapq
import math


def primes(limit: int) -> list[int]:
    composites: list[tuple[int, int]] = []
    ans: list[int] = []
    n = int(math.sqrt(limit + 1))

    for i in range(2, limit + 1):
        if not composites or composites[0][0] != i:
            ans.append(i)
            x = i * i
            if i <= n:
                heapq.heappush(composites, (x, i))
        else:
            while composites and composites[0][0] == i:
                x, y = heapq.heappop(composites)
                heapq.heappush(composites, (x + y, y))

    return ans
