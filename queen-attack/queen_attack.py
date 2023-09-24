from __future__ import annotations


class Queen:
    def __init__(self, row: int, column: int) -> None:
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.col = column

    def can_attack(self, another_queen: Queen) -> bool:
        if self == another_queen:
            raise ValueError("Invalid queen position: both queens in the same square")
        r = abs(self.row - another_queen.row)
        c = abs(self.col - another_queen.col)
        return r == 0 or c == 0 or r == c

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Queen):
            return False
        return self.row == other.row and self.col == other.col
