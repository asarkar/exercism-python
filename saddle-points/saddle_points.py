import itertools


def saddle_points(matrix: list[list[int]]) -> [dict[str, int]]:
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    if not all(len(r) == n for r in matrix):
        raise ValueError("irregular matrix")
    row_max = [max(r) for r in matrix]
    col_min = [min(matrix[r][c] for r in range(m)) for c in range(n)]

    return [
        {"row": r + 1, "column": c + 1}
        for r, c in itertools.product(range(m), range(n))
        if row_max[r] <= matrix[r][c] <= col_min[c]
    ]
