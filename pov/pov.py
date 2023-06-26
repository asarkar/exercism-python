from __future__ import annotations


class Tree:
    def __init__(self, label: str, children: list[Tree] = None) -> None:
        self.label = label
        self.children = children or []

    def __repr__(self) -> str:
        return f"Tree('{self.label}', {self.children})"

    def __lt__(self, other: Tree) -> bool:
        return self.label < other.label

    def __eq__(self, other: Tree) -> bool:
        return self.label == other.label and sorted(self.children) == sorted(other.children)

    def from_pov(self, from_node: str) -> Tree:
        if tree := self.pov(None, from_node):
            return tree
        raise ValueError("Tree could not be reoriented")

    # For example, if we have 0 - 1 - 2, and we are reorienting
    # on node 2, then node 2 is now the parent of node 1.
    #
    # Thus, each recursive call creates a node with the value of
    # the current node, adds the parent node to its children, and
    # removes the child node for which the recursive call is made
    # from the children.
    def pov(self, parent: Tree | None, target: str) -> Tree | None:
        p = [] if not parent else [parent]
        if self.label == target:
            return Tree(target, p + self.children)
        for x in self.children:
            all_but_x = [c for c in self.children if c.label != x.label]
            if result := x.pov(Tree(self.label, p + all_but_x), target):
                return result

        return None

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        if path := self.from_pov(from_node).path(to_node):
            return path
        raise ValueError("No path found")

    def path(self, target: str) -> list[str]:
        if self.label == target:
            return [target]
        for c in self.children:
            if result := c.path(target):
                return [self.label] + result
        return []
