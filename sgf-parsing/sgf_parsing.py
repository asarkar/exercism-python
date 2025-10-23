from __future__ import annotations

import dataclasses

from char_reader import CharReader


@dataclasses.dataclass
class SgfTree:
    properties: dict[str, list[str]] = dataclasses.field(default_factory=dict)
    children: list[SgfTree] = dataclasses.field(default_factory=list)


def parse(s: str) -> SgfTree:
    reader = CharReader(s)
    tree = Parser(reader).parse_tree()
    assert reader.is_eof(), "input not fully consumed"
    return tree


# GameTree   	= '(' Node+ GameTree* ')'
# Node       	= ';' Property*
# Property   	= PropId PropVal+
# PropId  		= Letter+
# Letter   		= 'A'..'Z'
# PropVal  		= '[' Text ']'


class Parser:
    def __init__(self, reader: CharReader):
        self.reader = reader

    # https://www.hexwiki.net/index.php/Smart_Game_Format#Tree_structure
    def parse_tree(self) -> SgfTree:
        if self.reader.next() != "(":
            raise ValueError("tree missing")

        prev = head = self.parse_node()

        # Parse additional nodes
        while self.reader.peek() == ";":
            node = self.parse_node()
            prev.children.append(node)
            prev = node

        # Parse nested trees
        while self.reader.peek() == "(":
            prev.children.append(self.parse_tree())

        # Discard ')
        while self.reader.peek() == ")":
            _ = self.reader.next()
        return head

    def parse_node(self) -> SgfTree:
        if self.reader.next() != ";":
            raise ValueError("tree with no nodes")

        return SgfTree(self.parse_properties())

    def parse_properties(self) -> dict[str, list[str]]:
        p: dict[str, list[str]] = {}
        p_id = self.parse_id()
        if not p_id:
            return p

        p[p_id] = self.parse_values()
        while self.reader.peek().isalpha():
            p.update(self.parse_properties())
        return p

    def parse_id(self) -> str:
        txt = []
        while (c := self.reader.peek()).isalpha():
            if c.islower():
                raise ValueError("property must be in uppercase")
            txt.append(self.reader.next())

        return "".join(txt)

    def parse_values(self) -> list[str]:
        if self.reader.next() != "[":
            raise ValueError("properties without delimiter")

        txt: list[str] = []
        escaped = False
        # Parse single character. There is a test that requires escaped
        # newline gets replaced with nothing, everything else is replaced
        # by usual rules.
        while (c := self.reader.next()) != "]" or escaped:
            if escaped:
                _ = txt.pop()
            if escaped and c == "\n":
                txt.append("")
            else:
                txt.append(" " if c == "\t" else c)

            # '\' isn't escape character if it's been escaped
            escaped = c == "\\" and not escaped

        values = ["".join(txt)]
        while self.reader.peek() == "[":
            values.extend(self.parse_values())
        return values
