import re


def answer(question: str) -> int:
    result = -1
    i = 0
    for m in re.finditer(r"([^0-9\-]+)(-?\d+)", question):
        if len(m.groups()) != 2:
            raise ValueError("syntax error")
        op = m.group(1).strip()
        i = int(m.group(2))

        if op == "What is":
            result = i
        elif op == "plus":
            result += i
        elif op == "minus":
            result -= i
        elif op == "multiplied by":
            result *= i
        elif op == "divided by":
            result //= i
        else:
            raise ValueError("syntax error")

        i = m.end()

    # If the question isn't fully consumed (except '?'), there is an error.
    # The difference between 'syntax error' and 'unknown operation' seems to
    # be whether there are any unknown words. If we recognize all the words,
    # then it's a 'syntax error', else 'unknown operation'.
    if i != len(question) - 1:
        w = question[i:-1].strip()
        terms = r"What\sis|plus|minus|multiplied\sby|divided\sby"
        if re.match(rf"^(?:{terms}\s*)+$", w) is not None:
            raise ValueError("syntax error")

        raise ValueError("unknown operation")

    return result
