from __future__ import annotations

import dataclasses

NODE, EDGE, ATTR = range(3)


@dataclasses.dataclass
class Node:
    name: str
    attrs: dict[str, str]


@dataclasses.dataclass
class Edge:
    src: str
    dst: str
    attrs: dict[str, str]


# pylint: disable=R0903
class Graph:
    def __init__(self, data=None):
        if data is not None and not isinstance(data, list):
            raise TypeError("Graph data malformed")
        self.attrs = {}
        self.nodes = []
        self.edges = []
        if not data:
            return
        for item in data:
            if not isinstance(item, tuple) or len(item) < 3:
                raise TypeError("Graph item incomplete")
            if item[0] == ATTR:
                self.attrs |= Graph.__parse_attr(item)
            elif item[0] == NODE:
                self.nodes.append(Graph.__parse_node(item))
            elif item[0] == EDGE:
                self.edges.append(Graph.__parse_edge(item))
            else:
                raise ValueError("Unknown item")

    @staticmethod
    def __parse_attr(item) -> dict[str, str]:
        if not isinstance(item[1], str) or not isinstance(item[2], str):
            raise ValueError("Attribute is malformed")
        return {item[1]: item[2]}

    @staticmethod
    def __parse_node(item) -> Node:
        if not isinstance(item[1], str) or not isinstance(item[2], dict):
            raise ValueError("Node is malformed")
        return Node(*item[1:])

    @staticmethod
    def __parse_edge(item) -> Edge:
        if len(item) != 4 or any(not isinstance(x, str) for x in item[1:3]) or not isinstance(item[3], dict):
            raise ValueError("Edge is malformed")
        return Edge(*item[1:])
