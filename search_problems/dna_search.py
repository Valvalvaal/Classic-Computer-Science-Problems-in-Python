from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

# Type alias for codon and gene
Codon = (Nucleotide, Nucleotide, Nucleotide)
Gene = [Codon]

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def str_to_gene(str_gene: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(str_gene), 3):
        # ignore the one or two nucleotides left if gene is not complete
        if i + 2 >= len(str_gene):
            return gene
        codon: Codon = (
            Nucleotide[str_gene[i]], Nucleotide[str_gene[i+1]], Nucleotide[str_gene[i+2]])
        gene.append(codon)
    return gene


my_gene = str_to_gene(gene_str)
