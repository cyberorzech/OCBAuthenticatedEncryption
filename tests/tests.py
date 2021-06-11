from src.aes import *
from src.bit_operations import *
import pytest

from src.associated_data_hash import *


class TestBit_Operations:
    def test_zeros_with_invalid_arg(self):
        with pytest.raises(ValueError) as valinfo:
            zeros(0)
        assert "n argument must be greater than 0" in str(valinfo.value)

    def test_zeros_with_valid_arg(self):
        n = 128
        x = zeros(n)
        assert len(x) == n
        for i in range(0, len(x)):
            assert x[i] == "0"

    def test_ntz(self):
        assert ntz(128) == 7
        assert ntz(256) != 7

    # bitwise xor has two available functions
    def test_strxor(self):
        s = "101"
        t = "100"
        assert isinstance(strxor(s, t), str)

    def test_bytes_xor(self):
        y = bytes_xor(bytes("101", "utf-8"), bytes("100", "utf-8"))
        assert isinstance(y, bytes)

    def test_convert_string_to_bytes(self):
        str = "Test123"
        bytesStr = convert_string_to_bytes(str)
        assert isinstance(bytesStr, bytes)
        assert bytesStr == b"Test123"

    def test_convert_bytes_to_string(self):
        bytesStr = b"Test123"
        string = convert_bytes_to_string(bytesStr)
        assert isinstance(string, str)
        assert string == "Test123"

    def test_encode_bytes_string_to_base64(self):
        bytesStr = b"Test123"
        bytesEncoded = encode_bytes_string_to_base64(bytesStr)
        assert bytesEncoded == b"VGVzdDEyMw=="
        assert isinstance(bytesEncoded, bytes)

    def test_decode_base64_bytes_to_utf8_string(self):
        encodedBytes = b"VGVzdDEyMw=="
        decodedBytes = decode_base64_bytes_to_utf8_string(encodedBytes)
        assert isinstance(decodedBytes, str)
        assert decodedBytes == "VGVzdDEyMw=="

    def test_return_substring_of_string(self):
        substring = return_substring_of_string(
            str="10101000010100010000111", leftBound=2, rightBound=5
        )
        assert substring == "1010"
        assert isinstance(substring, str)

    def test_convert_string_to_integer(self):
        integer = convert_string_to_integer("110")
        assert integer == 6
        assert isinstance(integer, int)

    def test_convert_integer_to_string(self):
        string = convert_integer_to_string(6)
        assert string == "110"
        assert isinstance(string, str)


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
