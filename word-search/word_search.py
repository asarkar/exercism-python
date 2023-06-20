from collections import defaultdict, namedtuple
from typing import Optional
from enum import Enum, auto

Point = namedtuple('Point', ['row', 'col'])


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    NE = auto()
    SE = auto()
    NW = auto()
    SW = auto()


# pylint: disable=R0903
class WordSearch:
    def __init__(self, puzzle: list[str]):
        self.puzzle = puzzle
        self.start_indices = defaultdict(list)
        for i, row in enumerate(puzzle):
            for j, c in enumerate(row):
                self.start_indices[c].append((i, j))

    def search(self, word: str) -> Optional[tuple[Point, Point]]:
        if not word:
            return None

        for row, col in self.start_indices.get(word[0], []):
            if p := self.__search_end(word, 0, Point(row, col), set(), None):
                return Point(col, row), p
        return None

    # pylint: disable=R0913
    def __search_end(self, word: str, i: int, coord: Point,
                     visited: set[Point], direction: Direction) -> Optional[Point]:
        if i >= len(word) or coord in visited:
            return None
        if i == (len(word) - 1):
            return Point(coord.col, coord.row)

        visited.add(coord)
        row, col = coord
        candidates: list[tuple[Direction, tuple[int, int]]] = [
            (Direction.NORTH, (row - 1, col)),
            (Direction.SOUTH, (row + 1, col)),
            (Direction.EAST, (row, col + 1)),
            (Direction.WEST, (row, col - 1)),
            (Direction.NE, (row - 1, col + 1)),
            (Direction.SE, (row + 1, col + 1)),
            (Direction.NW, (row - 1, col - 1)),
            (Direction.SW, (row + 1, col - 1))
        ]

        neighbors = [c for c
                     in candidates
                     if c[1] != coord
                     and 0 <= c[1][0] < len(self.puzzle)
                     and 0 <= c[1][1] < len(self.puzzle[c[1][0]])
                     and self.puzzle[c[1][0]][c[1][1]] == word[i + 1]
                     and c[1] not in visited
                     and direction in {None, c[0]}]
        for d, (r, c) in neighbors:
            if p := self.__search_end(word, i + 1, Point(r, c), visited, d):
                return p

        visited.remove(coord)
        return None
