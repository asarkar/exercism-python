class Bitset:
    def __init__(self, size: int) -> None:
        self._bits = 0
        self._size = size

    def set(self, i: int) -> None:
        self._bits |= 1 << i

    def clear(self, i: int) -> None:
        self._bits &= ~(1 << i)

    def is_set(self, i: int) -> bool:
        return (self._bits & 1 << i) > 0

    def get_all_set(self) -> list[int]:
        return [i for i in range(self._size) if self.is_set(i)]


class Allergies:
    def __init__(self, score: int) -> None:
        allergies = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats",
        }
        bits = Bitset(8)
        # Max score if a person is allergic to everything.
        max_score = 255
        Allergies._can_make_sum(list(allergies.keys()), 0, score & max_score, bits, {})
        self._allergens = [allergies[pow(2, i)] for i in bits.get_all_set()]

    def allergic_to(self, item: str) -> bool:
        return item in self._allergens

    # Subset sum.
    @staticmethod
    def _can_make_sum(nums: list[int], i: int, remaining: int, bits: Bitset, memo: dict[tuple[int, int], bool]) -> bool:
        """
        Returns true is remaining can be made by the sum of a subset of the array nums[i:].
        The elements chosen are indicated by the corresponding set bits in the bitset
        """
        if remaining == 0:
            return True
        if i >= len(nums) or bits.is_set(i):
            return False
        key = (i, remaining)
        if key in memo:
            return memo[key]
        found = False
        if nums[i] <= remaining:
            # Include nums[i].
            bits.set(i)
            found = Allergies._can_make_sum(nums, i + 1, remaining - nums[i], bits, memo)
        if not found:
            # Exclude nums[i].
            bits.clear(i)
            found = Allergies._can_make_sum(nums, i + 1, remaining, bits, memo)
        memo[key] = found
        return found

    @property
    def lst(self) -> list[str]:
        return self._allergens
