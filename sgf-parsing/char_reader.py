class CharReader:
    def __init__(self, txt: str) -> None:
        self.txt = txt
        self.idx = 0

    def __repr__(self) -> str:
        return f"(txt={self.txt}, next={self.peek()})"

    def next(self) -> str:
        char = self.peek()
        self.idx += 1
        return char

    def peek(self) -> str:
        return "" if self.is_eof() else self.txt[self.idx]

    def is_eof(self) -> bool:
        return self.idx == len(self.txt)
