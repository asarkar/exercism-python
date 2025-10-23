class Allergies:
    def __init__(self, score: int) -> None:
        allergies = [
            "eggs",
            "peanuts",
            "shellfish",
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats",
        ]
        # // If the ith bit is set, the result is that 2^i (greater than 0)
        self.allergens = [allergies[i] for i in range(len(allergies)) if score & (1 << i) > 0]

    def allergic_to(self, item: str) -> bool:
        return item in self.allergens

    @property
    def lst(self) -> list[str]:
        return self.allergens
