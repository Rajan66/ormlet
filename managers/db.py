import logging

from psycopg import sql

from base import ConnectionManager


class DATA_TYPES:
    str = ("varchar", "VARCHAR")
    int = ("int", "INT")
    bool = ("boolean", "BOOLEAN")


class ModelManager:
    def __init__(self):
        pass

    def create_table(self, table_name, fields):
        # TODO: map the fields with enum?
        with ConnectionManager() as connection:
            query = """
                CREATE TABLE IF NOT EXISTS "%s" (
                    name VARCHAR,
                    age INT
                )
                """
            try:
                connection.cursor.execute(sql.SQL(query % table_name))
                connection.conn.commit()
                logging.info("Table creation successful")
            except Exception as ex:
                logging.error(f"Failed to create table {table_name}: {ex}")
                raise
