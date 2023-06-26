def to_rna(dna_strand: str) -> str:
    rna = []
    mapping = {"G": "C", "C": "G", "T": "A", "A": "U"}

    for c in dna_strand:
        if c in mapping:
            rna.append(mapping[c])
        else:
            rna.clear()
            break

    return "".join(rna)
