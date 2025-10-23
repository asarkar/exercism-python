from __future__ import annotations

import dataclasses
import functools
import typing

from lark import Lark, Token, Transformer, UnexpectedCharacters, UnexpectedToken


@dataclasses.dataclass
class SgfTree:
    properties: dict[str, list[str]] = dataclasses.field(default_factory=dict)
    children: list[SgfTree] = dataclasses.field(default_factory=list)


# GameTree   	= '(' Node+ GameTree* ')'
# Node       	= ';' Property*
# Property   	= PropId PropVal+
# PropId  		= Letter+
# Letter   		= 'A'..'Z'
# PropVal  		= '[' Text ']'


def parse(input_string: str) -> SgfTree:
    sgf_grammar = r"""
        tree: "(" node+ tree* ")"
        node: ";" property*
        property: PROP_ID PROP_VAL+
        PROP_ID: UCASE_LETTER+
        PROP_VAL: /\[(\\+.|[^]])+\]/

        %import common.UCASE_LETTER
    """
    parser = Lark(sgf_grammar, start="tree", parser="lalr")
    try:
        return SgfTransformer().transform(parser.parse(input_string))[0]
    except UnexpectedCharacters as uc:
        if "PROP_ID" in uc.allowed or "PROP_VAL" in uc.allowed:
            raise ValueError("property must be in uppercase") from uc
        raise ValueError("unexpected") from uc
    except UnexpectedToken as ut:
        if ut.expected == {"SEMICOLON"}:
            raise ValueError("tree with no nodes") from ut
        if ut.expected == {"LPAR"}:
            raise ValueError("tree missing") from ut
        if ut.expected == {"PROP_VAL"}:
            raise ValueError("properties without delimiter") from ut
        raise ValueError("unexpected") from ut


class SgfTransformer(Transformer[Token, list[SgfTree]]):
    Properties = dict[str, list[str]]

    @staticmethod
    def __replace(s: str) -> str:
        """
        Processes single character. There is a test that
        requires escaped newline gets replaced with nothing,
        everything else is replaced by usual rules.

        :param s: string to process, includes '[' and ']'.
        :return: string with some characters possibly replaced
        """
        escaped = False
        txt: list[str] = []
        for c in s[1:-1]:
            if escaped:
                _ = txt.pop()
            if escaped and c == "\n":
                txt.append("")
            else:
                txt.append(" " if c == "\t" else c)

            # '\' isn't escape character if it's been escaped
            escaped = c == "\\" and not escaped
        return "".join(txt)

    @staticmethod
    def property(prop: list[Token]) -> Properties:
        return {prop[0].value: [SgfTransformer.__replace(t.value) for t in prop[1:]]}

    @staticmethod
    def node(properties: list[Properties]) -> SgfTree:
        return SgfTree(functools.reduce(lambda acc, p: acc | p, properties, {}))

    @staticmethod
    def tree(nodes: list[SgfTree | list[SgfTree]]) -> list[SgfTree]:
        if not nodes:
            return [SgfTree()]

        # A node is either a single node tree returned
        # by the function 'node' or a child forest returned
        # by this function.
        # # https://www.hexwiki.net/index.php/Smart_Game_Format#Tree_structure
        for i in range(len(nodes) - 1):
            node = typing.cast(SgfTree, nodes[i])
            if isinstance(nodes[i + 1], SgfTree):
                node.children.append(typing.cast(SgfTree, nodes[i + 1]))
            else:
                node.children.extend(
                    [child[0] for child in typing.cast(list[list[SgfTree]], nodes[i + 1 :])]
                )
                break

        return typing.cast(list[SgfTree], nodes[:1])
