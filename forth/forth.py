import bisect
import operator
import re
from collections import defaultdict, deque
from collections.abc import Callable


class StackUnderflowError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class Forth:
    _ASCII_ALPHA = r"[A-Za-z]+"
    _BIN_OP = r"[+\-*\\]"
    WORD = rf"""
        ^  # assert position at the start
        :  # match literal ':'
        \s+
        (
          {_ASCII_ALPHA}(?:-{_ASCII_ALPHA})*  # word, may contains hyphens
          |
          {_BIN_OP}  # binary op
        )
        \s+
    """
    DEFN = r"([^;\s]+)"  # take until whitespace or ';'
    NUM = r"-?\d+"  # signed integer

    def __init__(self, input_data: list[str]):
        self.stack: deque[int] = deque()
        self.defn: dict[str, list[tuple[int, list[str]]]] = defaultdict(list)
        self.defn_id = 0

        for line in input_data:
            if (wd := Forth.parse_defn(line)) is not None:
                self.create_defn(*wd)
            else:
                for cmd in line.split():
                    c = cmd.upper()
                    if c in self.defn:
                        i = self.defn[c][-1][0]
                        for x in self.resolve_defn(i + 1, c):
                            self.run_built_in_cmd(x)
                    else:
                        self.run_built_in_cmd(c)

    # Parse ": word-name definition ;".
    @classmethod
    def parse_defn(cls, txt: str) -> tuple[str, list[str]] | None:
        if txt[0] != ":":
            return None
        if (m := re.match(cls.WORD, txt, re.VERBOSE)) is not None:
            word = m.group(1)
            p = re.compile(cls.DEFN)
            defn = p.findall(txt, m.end())
            return word, defn

        raise ValueError("illegal operation")

    def get_stack(self) -> list[int]:
        return list(reversed(self.stack))

    def create_defn(self, word: str, defn: list[str]) -> None:
        """
        Stores the definition as raw text, doesn't evaluate eagerly.
        Since a word may later be redefined, the definitions are stored
        with monotonically increasing ids, thus establishing a
        happens-before relationship between any two definitions.
        The latest definition is at the end.

        :param word: word
        :param defn: definition
        :return: nothing
        """
        self.defn_id += 1
        self.defn[word.upper()].append((self.defn_id, [d.upper() for d in defn]))

    def resolve_defn(self, i: int, word: str) -> deque[str]:
        """
        Resolves a definition by recursively replacing all
        user-defined words with built-in commands. If a word
        is not found in the dictionary, it could be a built-in
        word, or an invalid one, to be find out later when
        parsing it as a built-in word.

        Definitions are processed in the reverse order
        because later definitions may refer to earlier ones,
        like ": foo foo 1 + ;". The second "foo" must be
        resolved first.

        For each word in the definition, finds the definition
        with the greatest id that is smaller than the given
        word's id. That gives the latest definition at the
        time this definition of word existed.

        :param i: unique definition id
        :param word: word to be resolved
        :return: a list of built-in commands
        """
        w = word.upper()
        if w not in self.defn:
            return deque([w])
        j = bisect.bisect_left(self.defn[w], i, key=operator.itemgetter(0))
        j, definitions = self.defn[w][j - 1]
        result: deque[str] = deque()
        for k in range(len(definitions) - 1, -1, -1):
            commands = self.resolve_defn(j, definitions[k])
            # deque.extendleft() reverses the argument,
            # so, do it manually.
            for c in range(len(commands) - 1, -1, -1):
                result.appendleft(commands[c])
        return result

    def run_built_in_cmd(self, cmd: str) -> None:
        if re.match(Forth.NUM, cmd):
            self.stack.appendleft(int(cmd))
        elif len(cmd) == 1:
            self.run_bin_op(cmd)
        else:
            self.run_stack_op(cmd)

    def run_bin_op(self, cmd: str) -> None:
        op: Callable[[int, int], int] | None = None
        match cmd:
            case "+":
                op = operator.add
            case "-":
                op = operator.sub
            case "*":
                op = operator.mul
            case "/":
                op = operator.floordiv
        if op is not None:
            if len(self.stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            x = self.stack.popleft()
            y = self.stack.popleft()
            if cmd == "/" and x == 0:
                raise ZeroDivisionError("divide by zero")
            self.stack.appendleft(op(y, x))
        else:
            raise ValueError("undefined operation")

    def run_stack_op(self, cmd: str) -> None:
        try:
            match cmd:
                case "OVER":
                    x = self.stack.popleft()
                    y = self.stack[0]
                    self.stack.extendleft([x, y])
                case "SWAP":
                    x = self.stack.popleft()
                    y = self.stack.popleft()
                    self.stack.extendleft([x, y])
                case "DUP":
                    self.stack.appendleft(self.stack[0])
                case "DROP":
                    self.stack.popleft()
                case _:
                    raise ValueError("undefined operation")
        except IndexError as ie:
            raise StackUnderflowError("Insufficient number of items in stack") from ie


def evaluate(input_data: list[str]) -> list[int]:
    return Forth(input_data).get_stack()
