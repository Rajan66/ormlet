import logging

from psycopg import sql

from base.connection import ConnectionManager
from managers.queryset import QuerySet


class Manager:
    """Model-level query manager exposing get() and all()."""

    def __init__(self, model) -> None:
        self.model = model

    def get(self, *args, **kwargs):
        """Build a SELECT * query with WHERE conditions from kwargs.

        Returns the raw query string (not executed results).
        """
        queryset = QuerySet(self.model).get(args, **kwargs)
        with ConnectionManager() as connection:
            res = connection.cursor.execute(
                sql.SQL(queryset % self.model._tablename)
            )
            logging.info("Results retrieved.")
        return res.fetchone()

    def all(self):
        """
        Build a SELECT query via QuerySet.all(), execute it, and return rows.
        """
        queryset = QuerySet(self.model).all()
        with ConnectionManager() as connection:
            res = connection.cursor.execute(
                sql.SQL(queryset % self.model._tablename)
            )
            logging.info("Results retrieved.")

        # TODO: should return queryset obj instead of result
        return res.fetchall()
