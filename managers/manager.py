import logging

from psycopg import sql

from base.connection import ConnectionManager
from managers.queryset import QuerySet


class Manager:
    def __init__(self, model) -> None:
        self.model = model

    def get(self, *args, **kwargs):
        queryset = QuerySet(self.model).get(args, kwargs)
        return queryset

    def all(self):
        queryset = QuerySet(self.model).all()
        with ConnectionManager() as connection:
            res = connection.cursor.execute(
                sql.SQL(queryset % self.model._tablename)
            )
            logging.info("Results retrieved...")

        # TODO: should return queryset obj instead of result
        return res.fetchall()
