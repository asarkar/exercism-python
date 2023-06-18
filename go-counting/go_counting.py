from collections import deque, defaultdict

WHITE = 'W'
BLACK = 'B'
NONE = ''

BLANK = ' '


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: list[str]):
        self.field = [[*row] for row in board]

    # Technically, a territory consists of all the cells that are
    # connected, i.e., it is possible to start from any one and
    # reach another. Thus, BFS/Union-Find can be used to find
    # a territory. We launch the search repeatedly from a blank
    # cell, and collect the results.
    #
    # The 'color' of a cell is determined by the color of its
    # neighboring occupied cells. If there's no occupied cell
    # nearby, the color of this cell is none. If there are more
    # than one colors of neighboring cells, then also the color
    # of this cell is none (not owned by either black or white).
    # If all the neighboring cells are of the same color, then
    # this cell picks up that color.
    #
    # Note that once a color has been determined for the territory,
    # it's never changed, and all later cells pick up the same color.
    def territory(self, x: int, y: int) -> tuple[str, set[tuple[int, int]]]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if 0 <= y < len(self.field) and 0 <= x < len(self.field[y]):
            # If we launch from an already visited cell,
            # we get an empty territory.
            if self.field[y][x] != BLANK:
                return NONE, set()
            return self.__bfs((y, x))
        raise ValueError('Invalid coordinate')

    def territories(self) -> dict[str, set[tuple[int, int]]]:
        """Find the owners and the territories of the whole board

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result = defaultdict(set)
        for i, row in enumerate(self.field):
            n = len(row)
            for col in range(n):
                if row[col] == BLANK:
                    color, territory = self.territory(col, i)
                    result[color].update(territory)
        return result

    def __bfs(self, start: tuple[int, int]) -> tuple[str, set[tuple[int, int]]]:
        q = deque([start])
        color = None
        visited = set()

        while q:
            row, col = q.popleft()
            if self.field[row][col] != BLANK:
                continue
            visited.add((col, row))
            candidates = [
                (row - 1, col),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col)
            ]
            neighbors = [c for c
                         in candidates
                         if 0 <= c[0] < len(self.field) and
                         0 <= c[1] < len(self.field[c[0]])]
            colors = {c for x
                      in neighbors
                      if (c := self.field[x[0]][x[1]]) != BLANK}
            if len(colors) == 1 and color in {(c := colors.pop()), None}:
                color = c
            else:
                color = NONE
            self.field[row][col] = color
            empties = [x for x
                       in neighbors
                       if self.field[x[0]][x[1]] == BLANK]
            q.extend(empties)

        return color, visited
