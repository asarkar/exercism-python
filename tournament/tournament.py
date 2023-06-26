class Result:
    def __init__(self, name: str) -> None:
        self.wins = self.losses = self.draws = 0
        self.name = name

    def matches_played(self) -> int:
        return self.wins + self.losses + self.draws

    def points(self) -> int:
        return self.wins * 3 + self.draws

    def __repr__(self) -> str:
        return (
            f"{self.name:<30} |{self.matches_played():>3} | {self.wins:>2} | "
            f"{self.draws:>2} | {self.losses:>2} | {self.points():>2}"
        )


def tally(rows: list[str]) -> list[str]:
    results = {}
    for r in rows:
        team1, team2, result = r.split(sep=";")
        if team1 not in results:
            results[team1] = Result(team1)
        if team2 not in results:
            results[team2] = Result(team2)

        if result == "win":
            results[team1].wins += 1
            results[team2].losses += 1
        elif result == "loss":
            results[team2].wins += 1
            results[team1].losses += 1
        else:
            results[team1].draws += 1
            results[team2].draws += 1

    out = [f"{'Team':<30} |{'MP':>3} | {'W':>2} | {'D':>2} | {'L':>2} | {'P':>2}"]
    xs = list(results.items())
    xs.sort(key=lambda x: (-x[1].points(), x[0]))
    for _, x in xs:
        out.append(str(x))
    return out
