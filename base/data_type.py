from enum import Enum


class DatabaseDataType(Enum):
    """Map ORM field class names to Postgres column types.

    A StrEnum so members compare equal to their string values, letting
    Field.get_column_type() return the member directly.

    Member names must match Field subclass names exactly, since
    Field.get_internal_type() returns self.__class__.__name__ and looks it up
    via DatabaseDataType[...] — a mismatch raises KeyError.
    """

    IntegerField = "INTEGER"
    CharField = "VARCHAR"
    BooleanField = "BOOLEAN"
