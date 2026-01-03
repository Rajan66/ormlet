import logging

from dotenv import load_dotenv

from base import Logger
from examples.user import User

# from helpers.model import ModelHelper
from managers import ModelManager

load_dotenv()


def main():
    Logger.configure()
    model_manager = ModelManager()

    try:
        model_manager.create_table(User._tablename, User._fields)
    except Exception as ex:
        logging.critical(f"Connection Failed: {ex}")
        raise


if __name__ == "__main__":
    main()
