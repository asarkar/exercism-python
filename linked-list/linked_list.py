from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Node:
    val: int
    prev: Node | None
    nxt: Node | None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def _singleton(self, val: int) -> None:
        self.head = self.tail = Node(val, None, None)
        self.size = 1

    def push(self, val: int) -> None:
        """
        Appends the given value at the end

        :param val: value to append
        :return: nothing
        """
        match self.tail:
            case None:
                self._singleton(val)
            case x:
                self.tail = Node(val, x, x.nxt)
                x.nxt = self.tail
                self.size += 1

    def pop(self) -> int:
        """
        Removes the last element of the list or raises ValueError if empty

        :return: the element removed
        """
        match self.tail:
            case None:
                raise IndexError("List is empty")
            case x:
                self.tail = x.prev
                if self.tail is not None:
                    self.tail.nxt = None
                else:
                    self.head = None
                self.size -= 1

                return x.val

    def shift(self) -> int:
        """
        Removes the first element of the list or raises ValueError if empty

        :return: the element removed
        """
        match self.head:
            case None:
                raise IndexError("List is empty")
            case x:
                self.head = x.nxt
                if self.head is not None:
                    self.head.prev = None
                else:
                    self.tail = None
                self.size -= 1

                return x.val

    def unshift(self, val: int) -> None:
        """
        Prepends the given value at the beginning

        :param val: value to prepend
        :return: nothing
        """
        match self.head:
            case None:
                self._singleton(val)
            case x:
                self.head = Node(val, x.prev, x)
                x.prev = self.head
                self.size += 1

    def delete(self, val: int) -> None:
        """
        Removes the given value from the list or raises ValueError if not found

        :param val: value to remove
        :return: nothing
        """
        node = self.head
        while node is not None and node.val != val:
            node = node.nxt

        if node is None:
            raise ValueError("Value not found")

        match node:
            case self.head:
                self.shift()
            case self.tail:
                self.pop()
            case _:
                if node.prev is not None:
                    node.prev.nxt = node.nxt
                if node.nxt is not None:
                    node.nxt.prev = node.prev

                self.size -= 1

    def __len__(self) -> int:
        return self.size
