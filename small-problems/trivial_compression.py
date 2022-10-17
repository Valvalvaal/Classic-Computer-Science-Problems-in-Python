from secrets import token_bytes


class CompressedGene:
    def __init__(self, gene: str) -> None:
        # ._method() Indicates it should only be used inside this class (private method)
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string = 1  # start with sentinel

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

    def decompress(self) -> str:
        gene = ""
        # jump every two bits, exclude sentinel with -1
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11  # gets last two bits comparing with 0b11
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]

    def __str__(self):
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    # TEST with example
    original = "ACGTACGTGCTAGATGATATAACGCGCTGCCGTAGCTGACTAAATCTCGCGTATTATATATATA" * 100

    print(f"Original is {getsizeof(original)} bytes")
    # Compress
    compressed = CompressedGene(original)
    print(f"compressed is {getsizeof(compressed.bit_string)} bytes")
    # print(compressed)
    # Decompress
    print(
        f"Original and decompressed are the same: {original == compressed.decompress()}")
