from __future__ import annotations

import itertools
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


# pylint: disable=R0903
class InputCell(Cell):
    @Cell.value.setter
    def value(self, value: int) -> None:
        """
        Iteratively updates the compute cells that depend on this input cell.
        The catch here is to update the dependencies of a compute cell _before_
        updating it. We do that using a distance array populated by BFS and
        by maximizing the distance function. What we are after is the _maximum_
        length of the path from a compute cell to this input cell.
        For example, in the graph below, both m3 and m4 are connected to
        cells of distance 1, but m4 is dependent on m3, and hence, must
        be updated after m3. m4 may initially be discovered from m1, and
        its distance set to 2, but will be later updated to 3 when we pop
        m3 from the queue and look at its children.

        It may be tempting to think that we can do a transitive reduction (TR)
        of the graph, but the TR for the below graph is the same as itself.
        https://en.wikipedia.org/wiki/Transitive_reduction

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

                dist = max(
                    distance.get(x, (-1, child))[0],
                    distance[id(cell)][0] + 1
                )
                distance[x] = (dist, child)

        for dist, group in itertools.groupby(
                sorted(distance.values(), key=lambda x: x[0]),
                key=lambda x: x[0]
        ):
            if dist == 0:  # Input cell
                continue
            for _, child in group:
                child.compute_value()


class ComputeCell(Cell):
    def __init__(
            self,
            dependencies: list[InputCell | ComputeCell],
            compute: Callable[[[int]], int],
    ):
        super().__init__()
        self._compute = compute
        self._callbacks = set()
        self._dependencies = dependencies
        for cell in dependencies:
            # Create a bidirectional link.
            cell.children.append(self)

        self.compute_value()

    def add_callback(self, callback: Callable[[int], None]) -> None:
        self._callbacks.add(callback)

    def remove_callback(self, callback: Callable[[int], None]) -> None:
        self._callbacks.discard(callback)

    def compute_value(self) -> None:
        new_value = self._compute([d.value for d in self._dependencies])
        if new_value != self._value:
            self._value = new_value
            for c in self._callbacks:
                c(self._value)
