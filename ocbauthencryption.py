from src.logger import *

DEBUG = 10
INFO = 20
ERROR = 40


def main():
    logger = Logger()
    logger.create_log(INFO, "OCB Authenticated Encryption script has started.")


if __name__ == "__main__":
    main()
