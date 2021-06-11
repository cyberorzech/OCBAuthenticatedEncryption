import codecs
import base64
from src.logger import *
from src.associated_data_hash import *
from src.aes import *
from src.bit_operations import *

DEBUG = 10
INFO = 20
ERROR = 40


def main():
    logger = Logger()
    logger.create_log(INFO, "OCB Authenticated Encryption script has started.")


if __name__ == "__main__":
    main()
