from __future__ import annotations
from typing import Optional
import dataclasses


@dataclasses.dataclass
class Node:
    val: int
    prev: Optional[Node] = None
    nxt: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def push(self, val: int) -> None:
        """
        Appends the given value at the end

        :param val: value to append
        :return: nothing
        """
        node = Node(val)
        self.size += 1
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.nxt = node
            node.prev = self.tail
            self.tail = node

    def pop(self) -> int:
        """
        Removes the last element of the list or raises ValueError if empty

        :return: the element removed
        """
        if self.is_empty():
            raise IndexError("List is empty")
        self.size -= 1
        prev = self.tail.prev
        node = self.tail
        node.prev = None
        if prev:
            prev.nxt = None
        else:
            self.head = None
        self.tail = prev
        return node.val

    def shift(self) -> int:
        """
        Removes the first element of the list or raises ValueError if empty

        :return: the element removed
        """
        if self.is_empty():
            raise IndexError("List is empty")
        self.size -= 1
        nxt = self.head.nxt
        node = self.head
        node.nxt = None
        if nxt:
            nxt.prev = None
        else:
            self.tail = None
        self.head = nxt
        return node.val

    def unshift(self, val: int) -> None:
        """
        Prepends the given value at the beginning

        :param val: value to prepend
        :return: nothing
        """
        node = Node(val)
        self.size += 1
        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.nxt = self.head
            self.head = node

    def delete(self, val: int) -> None:
        """
        Removes the given value from the list or raises ValueError if not found

        :param val: value to remove
        :return: nothing
        """
        node = self.head
        prev = None
        while node and node.val != val:
            prev = node
            node = node.nxt

        if not node:
            raise ValueError("Value not found")

        if node is self.head:
            self.shift()
        elif node is self.tail:
            self.pop()
        else:
            if prev:
                prev.nxt = node.nxt
            if node.nxt:
                node.nxt.prev = prev

            self.size -= 1

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size
