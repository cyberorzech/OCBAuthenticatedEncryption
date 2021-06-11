from src.aes import *
from src.bit_operations import *
import pytest

from src.associated_data_hash import *


class TestBit_Operations:
    def test_zeros_with_invalid_arg(self):
        with pytest.raises(ValueError) as valinfo:
            zeros(0)
        assert "n argument should be greater than 0" in str(valinfo.value)

    def test_zeros_with_valid_arg(self):
        n = 128
        x = zeros(n)
        assert len(x) == n
        for i in range(0, len(x)):
            assert x[i] == "0"


class TestAssociated_Data_Hash:
    def test_hash_when_A_is_null(self):
        K = BitArray(
            bin="1101 0011 0000 1100 1101 0011 0000 1100 1101 0011 0000 1100 1101 0011 0000 1100 1101 0011 0000 1100 1101 0011 0000 1100 1101 0011 0000 1100 1101 0011 0000 1100"
        )
        A = BitArray(bin="")
        zeros128 = str()
        ones128 = str()
        for i in range(0, 128):
            zeros128 += "0"
        for i in range(0, 128):
            ones128 += "1"
        assert hash(K, A) == BitArray(bin=zeros128)
        assert hash(K, A) != BitArray(bin=ones128)


class TestAES:
    def test_AES128_when_data_is_valid(self):
        # AES encryption routine example
        messageToEncrypt = "#test@12345"
        cipher = AESCipher("enIntVecTest2021")
        encrypted = cipher.encrypt(messageToEncrypt)
        encryptedString = encrypted.decode("utf-8")
        decrypted = cipher.decrypt(encrypted)
        assert decrypted == messageToEncrypt
        assert messageToEncrypt != encryptedString

    # def test_one(self):
    #     x = "this"
    #     assert "h" in x

    # def test_three(self):
    #     with pytest.raises(RuntimeError) as excinfo:

    #         def f():
    #             f()

    #         f()
    #     assert "maximum recursion" in str(excinfo.value)
