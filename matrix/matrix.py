class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self._rows: list[list[int]] = []
        self._cols: list[list[int]] = []

        for row_idx, row in enumerate(matrix_string.splitlines()):
            self._rows.append([])
            for col_idx, item in enumerate(row.split()):
                i = int(item)
                self._rows[-1].append(i)
                if col_idx >= len(self._cols):
                    self._cols.append([])
                self._cols[col_idx].append(i)

    def row(self, index: int) -> list[int]:
        return self._rows[index - 1]

    def column(self, index: int) -> list[int]:
        return self._cols[index - 1]
