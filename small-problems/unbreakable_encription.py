from secrets import token_bytes
from typing import Tuple


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string = 1  # start with sentinel
        print(self.bit_string)
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits | * 2^2
            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide: {nucleotide}")


def random_key(length: int) -> int:

    pass
