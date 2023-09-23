from __future__ import annotations

import typing
from typing import Optional, TypeAlias
import dataclasses
from enum import Enum, auto

Tree: TypeAlias = dict[str, "TreeValue"]
TreeValue: TypeAlias = int | None | Tree


@dataclasses.dataclass
class Node:
    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None

    @staticmethod
    def from_tree(tree: Optional[Tree]) -> Node | None:
        if tree is None:
            return None
        node = Node(typing.cast(int, tree["value"]))
        node.left = Node.from_tree(typing.cast(Optional[Tree], tree["left"]))
        node.right = Node.from_tree(typing.cast(Optional[Tree], tree["right"]))
        return node

    def to_tree(self) -> Tree:
        return {
            "value": self.value,
            "left": self.left.to_tree() if self.left is not None else None,
            "right": self.right.to_tree() if self.right is not None else None,
        }


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()


@dataclasses.dataclass
class Crumb:
    """
    Crumb consists of the value of the parent node,
    the direction taken to get to the focus node
    (left or right), and the other subtree.
    """

    value: int
    direction: Direction
    node: Optional[Node] = None


Breadcrumbs = list[Crumb]


class Zipper:
    """
    Heavily inspired by http://learnyouahaskell.com/zippers.
    A zipper is a combination of the "focus" node, and a
    directed path taken to get to it. The path is directed
    because it remembers the choice made at each node,
    i.e. going left or right.

    Every operation on a Zipper return a new Zipper.
    Although certainly possible, no mutations are done
    in the spirit of true functional programming
    (long live Haskell!).
    """

    def __init__(self, node: Node, breadcrumbs: Optional[Breadcrumbs] = None):
        assert node, "node must not be None"
        self.breadcrumbs = breadcrumbs or []
        self.node = node

    @staticmethod
    def from_tree(tree: Tree) -> Zipper:
        node = Node.from_tree(tree)
        assert node is not None
        return Zipper(node, [])

    def value(self) -> int:
        return self.node.value

    def set_value(self, value: int) -> Zipper:
        return Zipper(Node(value, self.node.left, self.node.right), self.breadcrumbs)

    def left(self) -> Zipper | None:
        if self.node.left:
            return Zipper(
                self.node.left,
                self.breadcrumbs + [Crumb(self.value(), Direction.LEFT, self.node.right)],
            )
        return None

    def set_left(self, node: Optional[Tree]) -> Zipper:
        return Zipper(Node(self.value(), Node.from_tree(node), self.node.right), self.breadcrumbs)

    def right(self) -> Zipper | None:
        if self.node.right:
            return Zipper(
                self.node.right,
                self.breadcrumbs + [Crumb(self.value(), Direction.RIGHT, self.node.left)],
            )
        return None

    def set_right(self, node: Optional[Tree]) -> Zipper:
        return Zipper(Node(self.value(), self.node.left, Node.from_tree(node)), self.breadcrumbs)

    def up(self) -> Zipper | None:
        if not self.breadcrumbs:
            return None
        parent = self.breadcrumbs[-1]
        bc = self.breadcrumbs[:-1]
        if parent.direction == Direction.LEFT:
            return Zipper(Node(parent.value, self.node, parent.node), bc)
        return Zipper(Node(parent.value, parent.node, self.node), bc)

    def to_tree(self) -> Tree:
        parent = self.up()
        return parent.to_tree() if parent else self.node.to_tree()
