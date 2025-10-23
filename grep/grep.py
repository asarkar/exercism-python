import re


def grep(pattern: str, flags: str, files: list[str]) -> str:
    filename = len(files) > 1
    line_numbers = "-n" in flags
    name_only = "-l" in flags

    pattern_txt = _build_pattern(pattern, flags)
    p = re.compile(rf"{pattern_txt}")
    result: list[str] = []

    for f in files:
        with open(f, encoding="UTF-8") as file:
            line_num = -1
            while line := file.readline().rstrip("\n"):
                line_num += 1
                if not re.search(p, line):
                    continue
                if name_only:
                    result.append(f)
                    break
                temp = []
                if filename:
                    temp.append(f"{f}:")
                if line_numbers:
                    temp.append(f"{line_num + 1}:")
                temp.append(line)
                result.append("".join(temp))

    return ("\n".join(result) + "\n") if result else ""


def _build_pattern(pattern: str, flags: str) -> str:
    case_insensitive = "-i" in flags
    invert = "-v" in flags
    whole_line = invert or "-x" in flags

    xs: list[str] = []
    if case_insensitive:
        xs.append("(?i)")
    if whole_line:
        xs.append("^")
    if invert:
        # Negative lookahead.
        # https://www.regular-expressions.info/lookaround.html
        xs.append(f"(?:(?!{pattern}).)*")
    else:
        xs.append(f"(?:{pattern})")
    if whole_line:
        xs.append("$")

    return "".join(xs)
