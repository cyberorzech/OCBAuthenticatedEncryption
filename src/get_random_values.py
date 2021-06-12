import uuid
import string
import random

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


# Input: none Output: string containing random upper/lower case letters, numbers and special chars
def key_gen_str(
    size=16,
    chars=string.ascii_uppercase
    + string.ascii_lowercase
    + string.punctuation
    + string.digits,
):
    return "".join(random.choice(chars) for _ in range(size))


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
