import itertools
import re
from collections import deque

BLANK = ' '
MINE = '*'


def annotate(minefield: list[str]) -> list[str]:
    field = [[*row] for row in minefield]
    n = -1
    for i, row in enumerate(field):
        if 0 <= n != len(row):
            raise ValueError('The board is invalid with current input.')
        n = len(row)
        for col in range(n):
            if row[col] == BLANK:
                __bfs(field, (i, col))
            elif not re.match(r'\*|\d+', row[col]):
                raise ValueError('The board is invalid with current input.')
    return [''.join(x) for x in field]


def __bfs(field: list[list[str]], start: tuple[int, int]) -> None:
    q = deque([start])
    while q:
        row, col = q.popleft()
        if field[row][col] != BLANK:
            continue
        candidates = itertools.product(
            [row, row - 1, row + 1],
            [col, col - 1, col + 1],
        )
        neighbors = [c for c
                     in candidates
                     if c != (row, col)
                     and 0 <= c[0] < len(field)
                     and 0 <= c[1] < len(field[c[0]])
                     and field[c[0]][c[1]] in {BLANK, MINE}]
        # Since we are processing row by row, column by column,
        # we don't need to look at previous cells.
        # Otherwise, we may run into an infinite loop where a
        # blank cell is repeatedly put on the queue.
        empties = [x for x
                   in neighbors
                   if field[x[0]][x[1]] == BLANK
                   and x[0] >= row
                   and x[1] >= col]
        num_mines = sum(1 for x
                        in neighbors
                        if field[x[0]][x[1]] == MINE)
        if num_mines:
            field[row][col] = str(num_mines)
        q.extend(empties)
