# https://exercism.org/tracks/python/exercises/killer-sudoku-helper/solutions/Hkishi
def combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]:
    if size == 1:
        return [[target]]

    result = []
    cage, remaining_target, remaining_size = [], target, size
    # Values bigger than half of target don't need to be tested
    # because if 4 + 6 = 10, so is 6 + 4.
    for i in range(1, min(10, target // 2)):
        # Ensure we don't include the same value twice in the cage.
        if i in exclude or i == remaining_target - i:
            continue
        if remaining_size == 2:
            cage.append(i)
            cage.append(remaining_target - i)
            result.append(cage)
            cage, remaining_target, remaining_size = [], target, size
        else:
            remaining_target -= i
            remaining_size -= 1
            cage.append(i)

    return result
