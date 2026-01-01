import logging
import sqlite3
from sqlite3 import DatabaseError


class ConnectionManager:
    """
    This is a context manager,
    for creating and closing connection,
    with the SQLite Database
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self):
        logging.info("Establishing the database connection....")
        try:
            self.con = sqlite3.connect(self.filename)
            self.cursor = self.con.cursor()
            return self
        except DatabaseError as ex:
            raise DatabaseError from ex

    def __exit__(self, type, value, traceback):
        logging.info("Closing the database connection....")
        self.con.close()
