from bitstring import BitStream, BitArray
from src.bit_operations import *

# Inputs: K - string of KEYLEN bits (key), A - string of any length (associated data)
def hash(K, A):
    if (len(A)) == 0:
        return BitArray(
            bin="0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000"
        )


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
