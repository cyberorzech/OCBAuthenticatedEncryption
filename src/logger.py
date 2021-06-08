import logging
import sys


class Logger:
    def __init__(self):
        logging.basicConfig(
            filename="logs/logs.log",
            format="%(asctime)s %(message)s",
            filemode="w",
        )
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Test messages
        # logger.debug("Harmless debug Message")
        # logger.info("Just an information")
        # logger.warning("Its a Warning")
        # logger.error("Did you try to divide by zero")
        # logger.critical("Internet is down")

    def create_log(self, level, message):
        self.logger.log(level, message)
        self.print_last_log()

    def print_last_log(self):
        with open("logs/logs.log", "r") as log_file:
            all_lines = log_file.readlines()
            print(all_lines[-1])

    def print_all_logs(self):
        with open("logs/logs.log", "r") as log_file:
            print(log_file.read())

    def exit_with_log(self):
        with open("logs/logs.log", "r") as log_file:
            print(log_file.read())
        exit()


def main():
    raise NotImplementedError("Not implemented yet.")


if __name__ == "__main__":
    main()
