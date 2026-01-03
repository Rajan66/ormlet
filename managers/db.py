import logging

from psycopg import sql

from base import ConnectionManager
from helpers.model import ModelHelper


class ModelManager:
    def __init__(self):
        pass

    def create_table(self, table_name, fields):
        with ConnectionManager() as connection:
            query = 'CREATE TABLE IF NOT EXISTS "%s"('
            columns = []
            constraints = ""

            for col_name, field_obj in fields.items():
                constraints = ModelHelper.get_column_constraints(
                    col_name,
                    field_obj,
                )
                columns.append(
                    f"{col_name} {field_obj.get_column_type()} {constraints}"
                )

            query += ",".join(columns) + ");"

            try:
                connection.cursor.execute(sql.SQL(query % table_name))
                connection.conn.commit()
                logging.info("Table creation successful")
            except Exception as ex:
                logging.error(f"Failed to create table {table_name}: {ex}")
                raise
