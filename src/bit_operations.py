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


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
