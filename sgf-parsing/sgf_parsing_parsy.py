from __future__ import annotations

import dataclasses
import functools

from parsy import regex, seq, string, generate, any_char, test_char, ParseError


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

def replace(c: str) -> str:
    if c == '\n':
        return '\n'
    if c == '\t':
        return ' '
    return c


def error_msg(pe: ParseError) -> str:
    msg = str(pe)
    if msg.startswith("expected '('"):
        msg = 'tree missing'
    elif msg.startswith("expected ';'"):
        msg = 'tree with no nodes'
    elif pe.stream[pe.index].islower():
        msg = 'property must be in uppercase'
    else:
        msg = 'properties without delimiter'
    return msg


def parse(input_string: str) -> SgfTree:
    prop_id = regex(r'[A-Z]+')

    escaped = string('\\') >> any_char.map(lambda c: '' if c == '\n' else replace(c))
    other = test_char(lambda c: c != ']', 'other').map(replace)
    # Parse single character. There is a test that requires escaped
    # newline gets replaced with nothing, everything else is replaced
    # by usual rules.
    single = escaped | other
    prop_val = string('[') >> single.many().concat() << string(']')

    prop = seq(prop_id, prop_val.at_least(1)).combine(
        lambda x, y: {x: y}
    )

    @generate
    def node():
        yield string(';')
        props = yield prop.many()
        return SgfTree(functools.reduce(lambda acc, p: acc | p, props, {}))

    # node = string(';') >> prop.many()\
    #     .tag('properties')\
    #     .combine(lambda _, x: SgfTree(functools.reduce(lambda acc, p: acc | p, x, {})))
    # tree = forward_declaration()
    # tree.become(string('(') >> seq(nodes=node.at_least(1), forest=tree.many()) << string(')'))

    # https://www.hexwiki.net/index.php/Smart_Game_Format#Tree_structure
    @generate
    def tree():
        yield string('(')
        nodes = yield node.at_least(1)
        forest = yield tree.many()
        yield string(')')
        if not nodes:
            return SgfTree()
        nodes[-1].children = forest
        for i in range(len(nodes) - 1):
            nodes[i].children = [nodes[i + 1]]
        return nodes[0]

    try:
        return tree.parse(input_string)
    except ParseError as pe:
        raise ValueError(error_msg(pe)) from pe
