import re

HEADER_PATTERN = "(#{1,6}) (.+)"
LIST_PATTERN = r"\* (.+)"
BOLD_PATTERN = (r"__(.+)__", r"<strong>\1</strong>")
ITALIC_PATTERN = (r"_(.+)_", r"<em>\1</em>")


def parse_header(line: str) -> str:
    if m := re.match(HEADER_PATTERN, line):
        n = len(m.group(1))
        return f"<h{n}>{m.group(2)}</h{n}>"
    return ""


def parse_bold_and_italic(line: str) -> str:
    for p, repl in [BOLD_PATTERN, ITALIC_PATTERN]:
        line = re.sub(p, repl, line)
    return line


def parse_list(line: str) -> str:
    if m := re.match(LIST_PATTERN, line):
        content = parse_bold_and_italic(m.group(1))
        return f"<li>{content}</li>"
    return ""


def parse(markdown: str) -> str:
    lines = markdown.splitlines()
    result: list[str] = []
    in_list = False

    for line in lines:
        if header := parse_header(line):
            result.append(header)
        elif list_item := parse_list(line):
            if not in_list:
                in_list = True
                list_item = f"<ul>{list_item}"
            result.append(list_item)
        else:  # Paragraph
            if in_list:
                in_list = False
                result.append("</ul>")
            result.append(f"<p>{parse_bold_and_italic(line)}</p>")

    # This is needed when the text ends with a list item.
    if in_list:
        result.append("</ul>")

    return "".join(result)
