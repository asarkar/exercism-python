import random


class Character:
    def __init__(self) -> None:
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> int:
        ds = random.choices(range(1, 7), k=4)
        return sum(ds) - min(ds)


def modifier(c: int) -> int:
    return (c - 10) // 2
