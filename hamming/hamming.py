def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(1 for (c1, c2) in zip(strand_a, strand_b) if c1 != c2)
