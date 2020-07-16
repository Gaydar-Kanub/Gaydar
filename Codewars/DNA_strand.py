def DNA_strand(dna: str) -> str:
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(d[i] for i in dna)


if __name__ == "__main__":
    print(DNA_strand("ATTGC"))