from __future__ import annotations
from typing import Optional
from collections.abc import Iterator


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.nxt: Optional[Node] = None

    def value(self) -> int:
        return self.val

    def next(self) -> Optional[Node]:
        return self.nxt


class LinkedList:
    def __init__(self, values: Optional[list[int]] = None) -> None:
        self.size = 0
        self.fst: Optional[Node] = None

        if values:
            for v in values:
                self.push(v)

    def __len__(self) -> int:
        return self.size

    def head(self) -> Node:
        if not self.fst:
            raise EmptyListException("The list is empty.")
        return self.fst

    def push(self, val: int) -> None:
        n = Node(val)
        n.nxt = self.fst
        self.fst = n
        self.size += 1

    def pop(self) -> int:
        if not self.fst:
            raise EmptyListException("The list is empty.")
        n = self.fst
        self.fst = n.nxt
        n.nxt = None
        self.size -= 1
        return n.value()

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if not self.fst:
            raise StopIteration
        x = self.fst.value()
        self.fst = self.fst.nxt
        return x

    def reversed(self) -> Iterator[int]:
        curr = self.fst
        values = []
        while curr:
            values.append(curr.value())
            curr = curr.nxt
        for index in range(len(values) - 1, -1, -1):
            yield values[index]


class EmptyListException(Exception):
    pass
