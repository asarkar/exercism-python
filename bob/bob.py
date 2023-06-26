def response(hey_bob: str) -> str:
    num_upper = num_lower = 0
    text = []
    for c in hey_bob:
        num_lower += int(c.islower())
        num_upper += int(c.isupper())
        if c.isalnum() or c == "?":
            text.append(c)

    question = text and text[-1] == "?"
    address = not text
    yell = num_upper and not num_lower

    if address:
        return "Fine. Be that way!"
    if yell and question:
        return "Calm down, I know what I'm doing!"
    if yell:
        return "Whoa, chill out!"
    if question:
        return "Sure."
    return "Whatever."
