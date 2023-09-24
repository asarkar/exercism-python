import random
import string


class Robot:
    def __init__(self) -> None:
        self._existing_names: set[str] = set()
        self.name = self._new_name()

    def _new_name(self) -> str:
        x = random.choices(string.ascii_uppercase, k=2)
        y = random.choices(string.digits, k=3)
        name = "".join(x + y)
        if name not in self._existing_names:
            self._existing_names.add(name)
            return name
        return self._new_name()

    def reset(self) -> None:
        self.name = self._new_name()
