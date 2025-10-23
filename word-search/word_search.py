from collections import namedtuple

# Tests expect this type.
Point = namedtuple("Point", ["row", "col"])


class WordSearch:
    def __init__(self, puzzle: list[str]) -> None:
        self.puzzle = puzzle
        self.m = len(puzzle)
        self.n = len(puzzle[0]) if self.m > 0 else 0
        # 8 possible search directions
        self.directions = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]

    # `solve` finds all words in the puzzle, returning start and end coordinates.
    def search(self, word: str) -> tuple[Point, Point] | None:
        for row in range(self.m):
            for col in range(self.n):
                if (
                    self.puzzle[row][col] == word[0]
                    and (end := self.find_word(word, row, col)) is not None
                ):
                    return Point(col, row), Point(end[0], end[1])

        return None

    # `find_word` checks all directions from a given starting point.
    def find_word(self, word: str, row: int, col: int) -> tuple[int, int] | None:
        for d in self.directions:
            if (end := self.follow(word, row, col, d)) is not None:
                return end
        return None

    # `follow` follows a fixed direction until the word is matched.
    def follow(self, word: str, r: int, c: int, dir: tuple[int, int]) -> tuple[int, int] | None:
        dr, dc = dir
        for i in range(1, len(word)):
            r += dr
            c += dc
            if r < 0 or r >= self.m or c < 0 or c >= self.n or self.puzzle[r][c] != word[i]:
                return None
        return c, r
