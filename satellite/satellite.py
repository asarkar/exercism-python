def tree_from_traversals(preorder: list[str], inorder: list[str]):
    pre = set(preorder)
    inorder_map = {x: i for i, x in enumerate(inorder)}
    if len(pre) != len(preorder) or len(inorder_map) != len(inorder):
        raise ValueError("traversals must contain unique items")
    if len(pre) != len(inorder_map):
        raise ValueError("traversals must have the same length")
    if pre != inorder_map.keys():
        raise ValueError("traversals must have the same elements")
    return __build(preorder, inorder_map, 0, 0, len(inorder) - 1)[0]


def __build(preorder: list[str], inorder_map: dict[str, int], i: int, lo: int, hi: int):
    """
    Builds a node.

    :param preorder: preorder traversal.
    :param inorder_map: mapping of node values to their
        corresponding indices in the inorder traversal.
    :param i: index into the preorder list.
    :param lo: start index into the inorder list.
    :param hi: end index into the inorder list.

    :returns: A 2-tuple consisting of the node, and the index
        into the preorder list up to which has been consumed.
    """
    if (lo > hi) or (i < 0) or (i > len(preorder) - 1):
        return {}, -1

    val = preorder[i]
    node = {"v": val, "l": {}, "r": {}}
    if lo == hi:
        return node, i + 1

    j = inorder_map[val]

    node["l"], x = __build(preorder, inorder_map, i + 1, lo, j - 1)
    node["r"], y = __build(preorder, inorder_map, max(x, i + 1), j + 1, hi)

    return node, max(x, y)
