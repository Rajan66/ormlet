import logging

from base import Logger
from managers import ConnectionManager


def main():
    Logger.configure()

    try:
        with ConnectionManager("test.db") as connection:  # noqa F401
            # connection.cursor.execute("CREATE TABLE NANI")
            logging.info("Creating database")
    except FileNotFoundError as ex:
        logging.error("Database file not found.")
        raise FileNotFoundError from ex
    except Exception as ex:
        raise Exception from ex


if __name__ == "__main__":
    main()
