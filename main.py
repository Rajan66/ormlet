import logging

from dotenv import load_dotenv

from base import Logger
from managers import ConnectionManager

load_dotenv()


def main():
    Logger.configure()

    try:
        with ConnectionManager() as conn:  # noqa F401
            try:
                logging.info("Creating table")
                # TODO: table creation not working, conn successful
                conn.cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS test_person(
                        name VARCHAR(50) UNIQUE NOT NULL,
                        age INT
                    )
                    """
                )
                conn.cursor.execute("SELECT to_regclass('test_person');")
                logging.info("Table created successfully...")
            except Exception as ex:
                logging.error(f"Failed to create table: {ex}")
                raise
    except Exception as ex:
        logging.critical(f"Connection Failed: {ex}")
        raise


if __name__ == "__main__":
    main()
