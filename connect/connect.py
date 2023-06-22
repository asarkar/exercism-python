from collections import deque


# pylint: disable=R0903
class ConnectGame:
    def __init__(self, board: str):
        self.field = [r.split() for r in board.splitlines()]

    def get_winner(self) -> str:
        player = 'O'
        top_os = ((0, c) for c in range(len(self.field[0])) if self.field[0][c] == player)
        if any(self.__bfs(o, player) for o in top_os):
            return player
        player = 'X'
        left_xs = [(r, 0) for r in range(len(self.field)) if self.field[r][0] == player]
        if any(self.__bfs(x, player) for x in left_xs):
            return player
        return ''

    def __bfs(self, start: tuple[int, int], player: str) -> bool:
        q = deque([start])
        while q:
            row, col = q.popleft()
            if self.field[row][col] != player:
                continue
            if player == 'O' and row == len(self.field) - 1:
                return True
            if player == 'X' and col == len(self.field[0]) - 1:
                return True
            self.field[row][col] = '.'
            candidates = [(row - 1, col),
                          (row - 1, col + 1),
                          (row, col - 1),
                          (row, col + 1),
                          (row + 1, col - 1),
                          (row + 1, col)
                          ]
            neighbors = [(r, c) for r, c
                         in candidates
                         if 0 <= r < len(self.field)
                         and 0 <= c < len(self.field[0])
                         and self.field[r][c] == player]
            q.extend(neighbors)

        return False
