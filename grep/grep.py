import re

import grep_test as gt  # type: ignore[import-not-found]


def grep(pattern: str, flags: str, files: list[str]) -> str:
    filename = len(files) > 1
    line_numbers = "-n" in flags
    name_only = "-l" in flags

    pattern_txt = __build_pattern(flags).replace("{}", pattern)
    p = re.compile(rf"{pattern_txt}")
    result = []

    for f in files:
        lines = gt.FILE_TEXT[f].splitlines()
        for line_num, line in enumerate(lines):
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


def __build_pattern(flags: str) -> str:
    case_insensitive = "-i" in flags
    invert = "-v" in flags
    whole_line = invert or "-x" in flags

    xs = []
    if case_insensitive:
        xs.append("(?i)")
    if whole_line:
        xs.append("^")
    if invert:
        # Negative lookahead.
        # https://www.regular-expressions.info/lookaround.html
        xs.append("(?:(?!{}).)*")
    else:
        xs.append("(?:{})")
    if whole_line:
        xs.append("$")

    return "".join(xs)
