def spiral_matrix(size: int) -> list[list[int]]:
    top_row = left_col = 0
    bottom_row = right_col = size - 1
    val = 0
    matrix = [[0] * size for _ in range(size)]

    while val < (size * size):
        # Fill top row.
        for col in range(left_col, right_col + 1):
            val += 1
            matrix[top_row][col] = val
        top_row += 1

        # Fill right column.
        for row in range(top_row, bottom_row + 1):
            val += 1
            matrix[row][right_col] = val
        right_col -= 1

        # Fill bottom row.
        for col in range(right_col, left_col - 1, -1):
            val += 1
            matrix[bottom_row][col] = val
        bottom_row -= 1

        # Fill left column.
        for row in range(bottom_row, top_row - 1, -1):
            val += 1
            matrix[row][left_col] = val
        left_col += 1

    return matrix
