import logging

from dotenv import load_dotenv

from base import Logger
from examples.person import Person
from helpers.model import ModelHelper
from managers import ModelManager

load_dotenv()


def main():
    Logger.configure()
    model_manager = ModelManager()

    model_name = ModelHelper.get_model_name(Person)
    model_fields = ModelHelper.get_model_fields(Person)

    try:
        model_manager.create_table(model_name, model_fields)
    except Exception as ex:
        logging.critical(f"Connection Failed: {ex}")
        raise


if __name__ == "__main__":
    main()
