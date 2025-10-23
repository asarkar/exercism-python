from __future__ import annotations


class TreeNode:
    def __init__(
        self, data: str, left: TreeNode | None = None, right: TreeNode | None = None
    ) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data: list[str]) -> None:
        self.root = None
        for x in tree_data:
            self.root = BinarySearchTree.__insert(self.root, x)

    def data(self) -> TreeNode | None:
        return self.root

    def sorted_data(self) -> list[str]:
        result: list[str] = []
        BinarySearchTree.__inorder(self.root, result)
        return result

    @staticmethod
    def __inorder(node: TreeNode | None, values: list[str]) -> None:
        if node is None:
            return
        BinarySearchTree.__inorder(node.left, values)
        values.append(node.data)
        BinarySearchTree.__inorder(node.right, values)

    @staticmethod
    def __insert(node: TreeNode | None, val: str) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if val <= node.data:
            node.left = BinarySearchTree.__insert(node.left, val)
        else:
            node.right = BinarySearchTree.__insert(node.right, val)
        return node
