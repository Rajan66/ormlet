import logging

import psycopg

from .env_config import config


class ConnectionManager:
    """Context manager for a Postgres connection.

    Opens a connection in ``__enter__`` and closes it when the ``with`` block
    exits. Credentials come from base.env_config.config.
    """

    def __init__(self) -> None:
        pass

    def __enter__(self):
        logging.info("Establishing the database connection....")
        self.conn = psycopg.connect(
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
        )
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, traceback):
        logging.info("Closing the database connection....")
        self.conn.close()
