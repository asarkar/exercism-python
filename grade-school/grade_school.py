from collections import defaultdict


class School:
    def __init__(self) -> None:
        self._roster: dict[int, set[str]] = defaultdict(set)
        self._added: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        if any(name in names for names in self._roster.values()):
            self._added.append(False)
            return
        self._roster[grade].add(name)
        self._added.append(True)

    def roster(self) -> list[str]:
        return [student for g in sorted(self._roster) for student in self.grade(g)]

    def grade(self, grade_number: int) -> list[str]:
        return sorted(self._roster[grade_number])

    def added(self) -> list[bool]:
        return self._added
