from abc import ABC

from base.data_type import DatabaseDataType


class Field(ABC):
    """Abstract base class for model fields.

    Stores field options and resolves the Postgres column type via
    DatabaseDataType.
    """

    def __init__(
        self,
        blank=False,  # only used in form validations so not used here
        null=False,  # whether the database should allow null or not
        db_index=False,
        unique=False,
        max_length=None,
        min_length=None,
        default=None,
    ):
        self.max_length = max_length
        self.min_length = min_length
        self.blank = blank
        self.null = null
        self.db_index = db_index
        self.unique = unique
        self.default = default

    def get_column_type(self):
        """Resolve the Postgres column type from DatabaseDataType."""
        return DatabaseDataType[self.get_internal_type()]

    def get_internal_type(self):
        """Return the Field subclass class name."""
        return self.__class__.__name__
