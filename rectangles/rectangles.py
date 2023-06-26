from collections import defaultdict
import itertools
import re


# A cool community solution: https://exercism.org/tracks/python/exercises/rectangles/solutions/pnowosie
def rectangles(strings: list[str]) -> int:
    # The argument to defaultdict needs to be a callable. A lambda is a callable.
    corners = defaultdict(lambda: defaultdict(list))

    # We create a mapping of column: (length, row) for every connected
    # horizontal side of the rectangle.
    # For example:
    #   +-+
    #   | |
    # +-+-+
    # | | |
    # +-+-+
    # produces
    #   2: {2: [0, 2, 4]} and
    #   0: {2: [2, 4], 4: [2, 4]}
    # The first record indicates that there are three sides
    # of length 2 that start at column 2, and these sides
    # are at rows 0, 2, and 4, respectively.
    for row, s in enumerate(strings):
        pluses = [m.start() for m in re.finditer("\\+", s)]
        for left_col, rt_col in itertools.combinations(pluses, 2):
            if re.fullmatch(r"\+[+-]*\+", s[left_col : rt_col + 1]):
                corners[left_col][rt_col - left_col + 1].append(row)

    num_rect = 0
    for col, segments in corners.items():
        # We consider the sides of equal length pairwise,
        # and check if the vertical columns are connected.
        # If yes, we got ourselves a rectangle.
        for length, rows in segments.items():
            for top_row, bottom_row in itertools.combinations(rows, 2):
                cols = [
                    f"{strings[row][col]}{strings[row][col + length - 1]}" for row in range(top_row, bottom_row + 1)
                ]
                if re.fullmatch(r"\+[+|]*\+", "".join(cols)):
                    num_rect += 1

    return num_rect
