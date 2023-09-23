from collections import deque
from enum import Enum, auto
from typing import NamedTuple


class Action(Enum):
    FILL_1 = auto()
    FILL_2 = auto()
    EMPTY_1 = auto()
    EMPTY_2 = auto()
    TXR_FROM_1_TO_2 = auto()
    TXR_FROM_2_TO_1 = auto()


class BucketStats(NamedTuple):
    num_moves: int
    goal_bucket: str
    other_bucket_capacity: int


class Move(NamedTuple):
    capacity1: int
    capacity2: int
    action: Action


def measure(capacity1: int, capacity2: int, goal: int, start_bucket: str) -> BucketStats:
    explored = set()
    frontier: deque[list[Move]] = deque()
    if start_bucket == "one":
        initial_move = Move(capacity1, 0, Action.FILL_1)
        forbidden_move = (0, capacity2)
    else:
        initial_move = Move(0, capacity2, Action.FILL_2)
        forbidden_move = (capacity1, 0)

    frontier.append([initial_move])

    while frontier:
        path = frontier.popleft()
        cap1, cap2, _ = path[-1]
        if cap1 == goal:
            return BucketStats(len(path), "one", cap2)
        if cap2 == goal:
            return BucketStats(len(path), "two", cap1)

        for move in __next_moves(cap1, cap2, capacity1, capacity2):
            m = (move[0], move[1])
            if m in explored or m == forbidden_move:
                continue
            explored.add(m)
            p = list(path)
            p.append(move)
            frontier.append(p)

    raise ValueError("Can't do it.")


def __next_moves(capacity1: int, capacity2: int, max_capacity1: int, max_capacity2: int) -> list[Move]:
    states: list[Move] = []

    if capacity1 > 0:
        states.append(Move(0, capacity2, Action.EMPTY_1))
    if capacity1 < max_capacity1:
        states.append(Move(max_capacity1, capacity2, Action.FILL_1))
        if capacity2 > 0:
            vol = min(max_capacity1 - capacity1, capacity2)
            states.append(Move(capacity1 + vol, capacity2 - vol, Action.TXR_FROM_2_TO_1))

    if capacity2 > 0:
        states.append(Move(capacity1, 0, Action.EMPTY_2))
    if capacity2 < max_capacity2:
        states.append(Move(capacity1, max_capacity2, Action.FILL_2))
        if capacity1 > 0:
            vol = min(max_capacity2 - capacity2, capacity1)
            states.append(Move(capacity1 - vol, capacity2 + vol, Action.TXR_FROM_1_TO_2))

    return states
