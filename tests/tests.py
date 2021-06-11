from src.aes import encryptDataAES128
import pytest

from src.associated_data_hash import *


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
    def test_AES128_when_data_is_too_long(self):
        with pytest.raises(ValueError) as valError:
            encryptDataAES128(data=b"Message that exceeds 16 bytes length")
            assert "16 byte boundary" in str(valError.value)

    def test_AES128_when_data_is_valid(self):
        encryptedMessageOne = encryptDataAES128(data=b"Sixteen bytedata")
        encryptedMessageTwo = encryptDataAES128(data=b"Sixteen bytedata")
        assert len(encryptedMessageOne) == 16
        assert type(encryptedMessageOne) == type(b"Bytes")
        assert encryptedMessageTwo != encryptedMessageOne

    # def test_one(self):
    #     x = "this"
    #     assert "h" in x

    # def test_three(self):
    #     with pytest.raises(RuntimeError) as excinfo:

    #         def f():
    #             f()

    #         f()
    #     assert "maximum recursion" in str(excinfo.value)
