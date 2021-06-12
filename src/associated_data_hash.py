from src.aes import AESCipher
from src.get_random_values import key_gen_str
from bitstring import BitStream, BitArray
from src.bit_operations import *

# Inputs: K - string of KEYLEN bits (key), A - string of any length (associated data)
def hash(K, A):
    if (len(A)) == 0:
        A_LENGTH = 128
        A = str()
        for x in range(0, A_LENGTH):
            A += "0"
        return A
    # Key-dependent variables
    L_star = create_L_star(K)  # Encrypts zeros(128) with random 128 bit key
    # L_dollar = double(L_star)     # TODO
    # L_0 = double(L_dollar)
    # L_i = double()

    # Consider A as a sequence of 128-bit blocks
    m = int(len(A) / 128)
    # Group A into 128 bit packages and the rest (A_*), which may be zero-length
    A_list = list()
    if m == 0:
        A_list += [A]
        return A_list
    if m > 0:
        for x in range(0, m):
            tmpStr = str()
            for y in range(x * 128, x * 128 + 128):
                tmpStr += A[y]
                if y == x * 128 + 128 - 1:
                    A_list += [tmpStr]
            if (
                x == m - 1
            ):  # If this is last 128-bit package, look if there are any bits remaining in string
                tmpStr = str()
                for y in range(x * 128 + 128, len(A)):
                    tmpStr += A[y]
                if len(tmpStr) > 0:
                    A_list += [tmpStr]
        return A_list


def create_L_star(K):
    plaintext = zeros(128)
    cipher = AESCipher(K)
    return cipher.encrypt(plaintext)


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
