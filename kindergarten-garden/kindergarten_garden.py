import bisect

PLANTS = {p[0]: p for p in ['Clover', 'Grass', 'Radishes', 'Violets']}


# pylint: disable=R0903
class Garden:
    def __init__(self, diagram: str, students: list[str] = None):
        if students:
            self.students = students
        else:
            self.students = [
                'Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry'
            ]

        self.students.sort()
        self.rows = diagram.splitlines()

    def plants(self, student: str) -> list[str]:
        i = bisect.bisect_left(self.students, student) * 2
        return [PLANTS[p] for row in self.rows for p in row[i: i + 2]]
