import uuid

# Input: none  Output: string containing random binary values
def key_gen():
    KEY_LENGTH = 128
    randomKey = str()
    for x in range(0, KEY_LENGTH):
        if get_inversion_bool(possibility=0.5) == True:
            randomKey += "1"
        else:
            randomKey += "0"
    return randomKey


def get_random_normalized_int128():
    tok = uuid.uuid4()
    return (tok.int % 100 + 1) / 100


def get_inversion_bool(possibility):
    if get_random_normalized_int128() >= possibility:
        return True
    else:
        return False


def main():
    raise NotImplementedError("Not implemented yet. Use as package.")


if __name__ == "__main__":
    main()
