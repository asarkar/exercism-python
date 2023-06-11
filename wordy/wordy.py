import re


def answer(question: str) -> int:
    p = re.compile(r'([^0-9\-]+)(-?\d+)')
    it = p.finditer(question)
    result = None
    i = 0
    for m in it:
        if len(m.groups()) != 2:
            raise ValueError('syntax error')
        op = m.group(1).strip()
        i = int(m.group(2))

        if op == 'What is':
            result = i
        elif op == 'plus':
            result += i
        elif op == 'minus':
            result -= i
        elif op == 'multiplied by':
            result *= i
        elif op == 'divided by':
            result //= i
        else:
            raise ValueError('syntax error')

        i = m.end()

    # If the question isn't fully consumed (except '?'), there is an error.
    # The difference between 'syntax error' and 'unknown operation' seems to
    # be whether there are any unknown words. If we recognize all the words,
    # then it's a 'syntax error', else 'unknown operation'.
    if i != len(question) - 1:
        w = question[i:-1].strip()
        if w in {'What is', 'plus', 'minus', 'multiplied by', 'divided by'}:
            raise ValueError('syntax error')

        raise ValueError('unknown operation')

    return result
