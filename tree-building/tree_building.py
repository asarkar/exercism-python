# pylint: disable=R0903
class Record:
    def __init__(self, record_id: int, parent_id: int) -> None:
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]) -> Node | None:
    if not records:
        return None
    records = sorted(records, key=lambda x: x.record_id)
    root = Node(records[0].record_id)
    if root.node_id != 0 or records[-1].record_id != len(records) - 1:
        raise ValueError("Record id is invalid or out of order.")
    if records[0].parent_id != records[0].record_id:
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    nodes = {0: root}
    for record in records[1:]:
        if record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        node = Node(record.record_id)
        if node.node_id in nodes:
            raise ValueError("Record id is invalid or out of order.")
        nodes[node.node_id] = node
        try:
            nodes[record.parent_id].children.append(node)
        except KeyError as exc:
            raise ValueError("Record id is invalid or out of order.") from exc
    return root
