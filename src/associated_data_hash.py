from bitstring import BitStream, BitArray
from src.bit_operations import *

# Inputs: K - string of KEYLEN bits (key), A - string of any length (associated data)
def hash(K, A):
    A_LENGTH = 128
    if (len(A)) == 0:
        A = str()
        for x in range(0, A_LENGTH):
            A += "0"
        return A
    # chyba trzeba zmienic A na string zwykly, a K generowac losowo i automatycznie


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
