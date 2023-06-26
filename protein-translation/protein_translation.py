from itertools import takewhile


def proteins(strand: str) -> list[str]:
    translations = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
    }
    chunk_size = 3
    xs = [strand[i : i + chunk_size] for i in range(0, len(strand), chunk_size)]
    ys = [translations.get(x, "STOP") for x in xs]
    return list(takewhile(lambda x: x != "STOP", ys))
