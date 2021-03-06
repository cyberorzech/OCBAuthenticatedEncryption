import codecs
import base64


# Input: integer    Output: string filled with zeros
def zeros(n):
    if n < 1:
        raise ValueError("bit_operations: zeros: n argument must be greater than 0.")
    result = ""
    for x in range(0, n):
        result += "0"
    return result


# Input: integer    Output: integer (the biggest x that returns integer for n/2**x)
def ntz(n):
    if n < 1:
        raise ValueError("bit_operations: ntz: n argument must not be less than 1. ")
    x = 0
    x = power(n, x)
    return x


# Input: integer, integer   Output: integer
def power(n, x):
    currentDivRes = n / 2 ** x
    if currentDivRes.is_integer():
        result = power(n, x + 1)
    else:
        return x - 1
    return result


# Input: string, string     Output: string (\x12-like values)
def strxor(s, t):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))


# Input: string, string     Output: string
def xor_of_two_128_bit_strings(left, right):
    result = str()
    for x in range(0, 128):
        if left[x] == right[x]:
            result += "0"
        else:
            result += "1"
    return result


# Input: bytes, bytes   Output: bytes
def bytes_xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def convert_string_to_bytes(str):
    return bytes(str, "utf-8")


def convert_bytes_to_string(bytesStr):
    return codecs.decode(bytesStr, "utf-8")


def encode_bytes_string_to_base64(strBytes):
    return base64.b64encode(strBytes)


def decode_base64_bytes_to_utf8_string(b64Bytes):
    return b64Bytes.decode("utf-8")


def return_substring_of_string(str, leftBound, rightBound):
    substring = ""
    for x in range(leftBound, rightBound + 1):  # right bound inclusive, hence +1
        substring += str[x]
    return substring


def convert_string_to_integer(str):
    return int(str, base=2)


def convert_integer_to_string(integer):
    return bin(integer)[2:]


def double(string):
    # double(S) == (S[2..128] || 0) xor (zeros(120) || 10000111)
    STRING_LENGTH = 128
    FIRST_ELEMENT = 0
    PADDING = "10000111"
    if len(string) != STRING_LENGTH:
        raise ValueError("String of bits must have an exact length of 128.")
    for x in range(FIRST_ELEMENT, STRING_LENGTH):
        if string[x] != "0" and string[x] != "1":
            raise ValueError("String of bits contains non binary values.")
    if string[FIRST_ELEMENT] == "0":
        return concatenate_string_and_zero(string)
    if string[FIRST_ELEMENT] == "1":
        leftXORElement = concatenate_string_and_zero(string)
        rightXORElement = zeros(120) + PADDING
        return xor_of_two_128_bit_strings(leftXORElement, rightXORElement)


def concatenate_string_and_zero(string):
    STRING_LENGTH = 128
    FIRST_ELEMENT = 0
    result = str()
    for x in range(FIRST_ELEMENT + 1, STRING_LENGTH):
        result += string[x]
    result += "0"
    return result


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
