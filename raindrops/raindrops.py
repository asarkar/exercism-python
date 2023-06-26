def convert(number: int) -> str:
    mapping = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    x = [s for (i, s) in mapping if number % i == 0]
    return "".join(x) if x else str(number)
