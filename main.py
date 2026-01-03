import logging

from dotenv import load_dotenv

from base import Logger
from examples.user import User
from helpers.model import ModelHelper
from managers import ModelManager

load_dotenv()


def main():
    Logger.configure()
    model_manager = ModelManager()

    model_name = ModelHelper.get_model_name(User)
    model_fields = ModelHelper.get_model_fields(User)

    try:
        model_manager.create_table(model_name, model_fields)
    except Exception as ex:
        logging.critical(f"Connection Failed: {ex}")
        raise


if __name__ == "__main__":
    main()
