from abc import ABC

from base.data_type import DatabaseDataType


class Field(ABC):
    def __init__(
        self,
        blank=False,  # only used in form validations so not used here
        null=False,  # whether the database should allow null or not
        db_index=False,
        unique=False,
        max_length=None,
        min_length=None,
    ):
        self.blank = blank
        self.null = null
        self.db_index = db_index
        self.unique = unique
        self.min_length = min_length
        self.max_length = max_length

    def get_column_type(self):
        return DatabaseDataType[self.get_internal_type()].value

    def get_internal_type(self):
        return self.__class__.__name__
