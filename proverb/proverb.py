import itertools


def proverb(*inputs: str, qualifier: str | None) -> list[str]:
    if not inputs:
        return []
    rhyme: list[str] = []
    for s, t in itertools.pairwise(inputs):
        rhyme.append(f"For want of a {s} the {t} was lost.")

    q = f" {qualifier}" if qualifier is not None else ""
    rhyme.append(f"And all for the want of a{q} {inputs[0]}.")
    return rhyme
