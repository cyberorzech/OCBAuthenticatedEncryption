from bitstring import INIT_NAMES
from src.aes import *
from src.bit_operations import *
from src.get_random_values import *
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
        with pytest.raises(ValueError) as valinfo:
            ntz(0)
        assert "n argument must not be less than 1" in str(valinfo.value)
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

    def test_double_if_string_is_too_short(self):
        with pytest.raises(ValueError) as valinfo:
            double("010010001010001111010100111")
        assert "String of bits must have an exact length of 128" in str(valinfo.value)

    def test_double_if_string_contains_non_binary_chars(self):
        with pytest.raises(ValueError) as valinfo:
            string = str()
            for x in range(0, 127):
                if x % 2 == 0:
                    string += "0"
                else:
                    string += "1"
            string += "z"
            double(string)
        assert "String of bits contains non binary values." in str(valinfo.value)

    def test_double_if_string_starts_with_0(self):
        string = "0"
        for x in range(1, 128):
            string += "1"
        result = double(string)
        for x in range(0, 127):
            assert result[x] == string[x + 1]
        assert result[127] == "0"
        stringInt = convert_string_to_integer(string)
        resultInt = convert_string_to_integer(result)
        assert stringInt * 2 == resultInt

    def test_double_if_string_starts_with_1(self):
        string = "1"
        for x in range(1, 128):
            string += "0"
        # left, right = double(string)      tests for xor
        # assert len(left) == 128 == len(right)
        # assert left[127] == "0" == right[119]
        # assert return_substring_of_string(right, 120, 127) == "10000111"
        result = double(string)
        assert isinstance(result, str)
        assert convert_string_to_integer(string) != convert_string_to_integer(
            result
        )  # check if this case is implemented correctly (TODO)


class TestAssociated_Data_Hash:
    def test_hash_when_A_is_null(self):
        K = key_gen_str()
        A = str()
        assert hash(K, A) == zeros(128)

    def test_hash_when_A_contain_3x128_bits(self):
        K = key_gen_str()
        A = str()
        for x in range(0, 3):
            A += key_gen()
        result = hash(K, A)
        assert isinstance(result, list)
        assert len(result) == 3
        for x in range(0, 3):
            assert len(result[x]) == 128

    def test_hash_when_A_contain_less_than_128_bits(self):
        K = key_gen_str()
        A = "10010101110110110001"
        result = hash(K, A)
        assert isinstance(result, list)
        assert len(result) == 1

    def test_hash_when_A_contain_more_than_3x128_bits(self):
        K = key_gen_str()
        A = str()
        rest = "100001010011110101100"
        for x in range(0, 3):
            A += key_gen()
        A += rest
        result = hash(K, A)
        assert isinstance(result, list)
        assert len(result) == 4
        assert result[3] == rest


class TestAES:
    def test_AES128_when_data_is_valid(self):
        # AES encryption routine example
        messageToEncrypt = "#test@12345"
        cipher = AESCipher(key_gen_str())
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


class TestGet_Random_Values:
    def test_key_gen(self):
        randomKey = key_gen()
        assert len(randomKey) == 128
        assert isinstance(randomKey, str)
        for x in range(0, 128):
            assert randomKey[x] == "0" or randomKey[x] == "1"

    def test_key_gen_str(self):
        randomKey = key_gen_str()
        assert len(randomKey) == 16
        assert isinstance(randomKey, str)
