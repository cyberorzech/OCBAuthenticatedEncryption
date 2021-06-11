import codecs
import base64
from src.logger import *
from src.associated_data_hash import *
from src.aes import *

DEBUG = 10
INFO = 20
ERROR = 40


def main():
    logger = Logger()
    logger.create_log(INFO, "OCB Authenticated Encryption script has started.")

    # AES encryption routine example
    cipher = AESCipher("enIntVecTest2021")
    encrypted = cipher.encrypt("#test@12345")
    print(encrypted.decode("utf-8"))
    decrypted = cipher.decrypt(encrypted)
    print(decrypted)


if __name__ == "__main__":
    main()
