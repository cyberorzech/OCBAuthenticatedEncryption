def zeros(n):
    if n < 1:
        raise ValueError("bit_operations: zeros: n argument must be greater than 0.")
    result = ""
    for x in range(0, n):
        result += "0"
    return result


def ntz(n):
    if n < 1:
        raise ValueError("bit_operations: ntz: n argument must not be less than 1. ")
    x = 0
    x = power(n, x)
    return x


def power(n, x):
    currentDivRes = n / 2 ** x
    if currentDivRes.is_integer():
        result = power(n, x + 1)
    else:
        return x - 1
    return result


def strxor(s, t):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))


def bytes_xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
