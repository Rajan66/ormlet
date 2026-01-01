import logging

import psycopg

from base import config


class ConnectionManager:
    """
    This is a context manager,
    for creating and closing connection,
    with the Postgres Database
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
