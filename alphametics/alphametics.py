def __parse(puzzle: str) -> tuple[list[str], str]:
    xs, result = [piece.strip() for piece in puzzle.split('==')]
    equation = [piece.strip()[::-1] for piece in xs.split('+')]
    return equation, result[::-1]


def solve(puzzle: str) -> dict[str, int]:  # noqa: C901
    equation, result = __parse(puzzle)
    if any(len(line) > len(result) for line in puzzle):
        raise ValueError('invalid equation')
    non_zero_letters = {line[-1] for line in equation}
    non_zero_letters.add(result[-1])

    # pylint: disable=R0911
    def can_solve(row: int, col: int, carry: int, solution: dict[str, int]) -> bool:
        addend = row < len(equation)
        word = equation[row] if addend else result
        n = len(word)

        if col >= n and addend:
            return can_solve(row + 1, col, carry, solution)

        if col == n and not addend:
            return carry == 0

        letter = word[col]
        assigned = letter in solution
        sum_digit = carry % 10

        # Addend
        if addend and assigned:
            return can_solve(row + 1, col, carry + solution[letter], solution)
        if addend:
            used = solution.values()
            unused = [i for i in range(10) if i not in used]
            for i in unused:
                if i == 0 and letter in non_zero_letters:
                    continue
                solution[letter] = i
                if can_solve(row + 1, col, carry + i, solution):
                    return True
                solution.pop(letter)
            return False
        # Result
        if assigned:
            return ((solution[letter] == sum_digit) and
                    can_solve(0, col + 1, carry // 10, solution))

        used = sum_digit in solution.values()
        if used or (sum_digit == 0 and letter in non_zero_letters):
            return False
        solution[letter] = sum_digit
        if can_solve(0, col + 1, carry // 10, solution):
            return True
        solution.pop(letter)
        return False

    xs = {}
    return xs if can_solve(0, 0, 0, xs) else None
