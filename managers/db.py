import logging

from psycopg import sql

from base import ConnectionManager


class ModelManager:
    def __init__(self):
        pass

    def create_table(self, table_name, fields):
        with ConnectionManager() as connection:
            query = 'CREATE TABLE IF NOT EXISTS "%s"('
            columns = ",".join(
                [
                    f"{col_name} {field_obj.get_column_type()}"
                    for col_name, field_obj in fields.items()
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
