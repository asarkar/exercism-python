class HighScores:
    def __init__(self, scores: list[int]) -> None:
        self.scores = scores

    def latest(self) -> int:
        assert self.scores
        return self.scores[-1]

    # This is the slowest method for calculating top-K,
    # but we are aiming for simplicity here.
    def personal_top_three(self) -> list[int]:
        return sorted(self.scores, reverse=True)[:3]

    def personal_best(self) -> int:
        assert self.scores
        return max(self.scores)
