from __future__ import annotations

import itertools
import sys
from collections import deque
from abc import ABC
from typing import Callable


# A cool community solution: https://exercism.org/tracks/python/exercises/react/solutions/rcardenes
class Cell(ABC):
    def __init__(self, value: int = None):
        if self.__class__ == Cell:
            raise TypeError('Cannot instantiate abstract class.')

        self._value = value
        self.children: list[ComputeCell] = []

    def __repr__(self) -> str:
        return f'{type(self).__name__}({self._value})'

    @property
    def value(self) -> int:
        return self._value


class InputCell(Cell):
    @Cell.value.setter
    def value(self, value: int) -> None:
        """
        Iteratively updates the compute cells that depend on this input cell.
        The catch here is to update the dependencies of a cell before updating it.
        To do that, we use a distance array populated by BFS. Then, all cells
        at the same distance are processed together. See the 'dist' function
        for an example.

        :param value: new value
        :return: nothing
        """
        self._value = value

        distance: dict[int, (int, Cell)] = {id(self): (0, self)}
        q: deque[Cell] = deque([self])
        while q:
            cell = q.popleft()
            for child in cell.children:
                x = id(child)
                if x not in distance:
                    q.append(child)

                dist = min(distance.get(x, (sys.maxsize, child))[0], distance[id(cell)][0] + 1)
                distance[x] = (dist, child)

        for dist, group in itertools.groupby(sorted(distance.values(), key=InputCell.dist), key=InputCell.dist):
            if dist == 0:  # Input cell
                continue
            for _, child in group:
                values = [distance[id(d)][1].value for d in child.dependencies]
                child.compute_value(values)

    @staticmethod
    def dist(x: (int, Cell)) -> int:
        """
        Returns the distance from the input cell. For cells at the same distance,
        uses the number of dependencies as a second factor. For example, both
        m3 and m4 have the same distance (=2) below according to BFS. In this
        case, we supplement the distance function by considering the number
        of outgoing edges.
                            ┌────┐
             ┌─────────────►│  i │◄──────────────────┐
             │              └────┘                   │
             │                                       │
             │                                       │
             │                                       │
             │                                       │
         ┌───┴───┐                               ┌───┴───┐
         │       │                               │       │
         │ i + 1 │                               │ i - 1 │
         │       │                               │       │
         └───────┘                               └───────┘
            m1▲                                      m2
              │                                      ▲
              │                                      │
              │                                      │
              │                                      │
        ┌─────┴─────┐                                │
        │           │                             ┌──┴────┐
        │           │                             │       │
        │  m1 * m3  ├─────────────────────────────► m2 - 1│
        │           │                             │       │
        │           │                             └───────┘
        └───────────┘                                m3
            m4

        :param x: 2-tuple of initial distance and cell
        :return: distance from the input cell
        """
        return 0 if isinstance(x[1], InputCell) else x[0] + len(x[1].dependencies)


class ComputeCell(Cell):
    def __init__(self, dependencies: list[InputCell | ComputeCell], compute: Callable[[[int]], int]):
        super().__init__()
        self._compute = compute
        self._callbacks = set()
        self.dependencies = dependencies
        values = []
        for cell in dependencies:
            # Create a bidirectional link.
            cell.children.append(self)
            values.append(cell.value)

        self.compute_value(values)

    def add_callback(self, callback) -> None:
        self._callbacks.add(callback)

    def remove_callback(self, callback) -> None:
        self._callbacks.discard(callback)

    def compute_value(self, values: list[int]) -> None:
        new_value = self._compute(values)
        if new_value != self._value:
            self._value = new_value
            for c in self._callbacks:
                c(self._value)
