import logging
from enum import Enum

from psycopg import sql

from base import ConnectionManager


class DATA_TYPES(Enum):
    str = "varchar"
    int = "int"
    bool = "boolean"


class ModelManager:
    def __init__(self):
        pass

    def create_table(self, table_name, fields):
        for key, value in fields.items():
            fields[key] = (
                DATA_TYPES[value].value
                if value in DATA_TYPES.__members__.keys()
                else value
            )

        with ConnectionManager() as connection:
            query = 'CREATE TABLE IF NOT EXISTS "%s"('
            columns = ",".join(
                [
                    f"{col_name} {col_type}"
                    for col_name, col_type in fields.items()
                ]
            )
            query += columns + ");"
            try:
                connection.cursor.execute(sql.SQL(query % table_name))
                connection.conn.commit()
                logging.info("Table creation successful")
            except Exception as ex:
                logging.error(f"Failed to create table {table_name}: {ex}")
                raise
