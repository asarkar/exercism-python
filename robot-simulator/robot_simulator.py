# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def move(self, instructions: str) -> None:
        for ins in instructions:
            if ins == "A":
                self._advance()
            else:
                self._turn(ins)

    def _advance(self) -> None:
        # match-case can't be used with unqualified names,
        # like the direction global constants here.
        # https://peps.python.org/pep-0636/#matching-against-constants-and-enums
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        elif self.direction == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        else:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

    def _turn(self, d: str) -> None:
        match d:
            case "L":
                self.direction = (self.direction - 1) if self.direction >= 1 else WEST
            case _:
                self.direction = (self.direction + 1) % 4
