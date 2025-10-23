from collections import deque
from collections.abc import Callable
from typing import Any


def encode(message: str, num_rails: int) -> str:
    rails: list[list[str]] = [[] for _ in range(num_rails)]
    # Populate the rails.
    __zigzag(message, num_rails, lambda i, ch: rails[i].append(ch))
    return "".join("".join(r) for r in rails)


def decode(encoded_message: str, num_rails: int) -> str:
    # Calculate the length of the rails.
    # Example: For cipher="WECRLTEERDSOEEFEAOCAIVDEN",
    # rail_lengths = [7, 12, 6].
    rail_lengths = [0] * num_rails
    __zigzag(
        encoded_message,
        num_rails,
        lambda i, _: rail_lengths.__setitem__(i, rail_lengths[i] + 1),
    )

    # Populate the rails.
    rails = []
    k = 0
    for i in rail_lengths:
        txt = encoded_message[k : k + i]
        rails.append(deque([*txt]))
        k += i

    # Decode using the starting indices of the rails.
    # 1st character of plain text is the 1st character
    # of rail 1, 2nd character of plain text is the
    # 1st character of rail 2, and so on.
    # As we read from a rail, we pop() the first character.
    # This is akin to merging k sorted lists.
    message = []
    __zigzag(encoded_message, num_rails, lambda x, _: message.append(rails[x].popleft()))

    return "".join(message)


def __zigzag(txt: str, num_rails: int, fn: Callable[[int, str], Any]) -> None:
    """Iterate over the rails in a zigzag manner,
    and invoke the given function for each rail and character.
    """
    rail_idx = 0
    step = -1

    for ch in txt:
        if ch.isspace():
            continue
        fn(rail_idx, ch)
        if rail_idx in {0, num_rails - 1}:
            step *= -1
        if num_rails > 1:
            rail_idx += step
