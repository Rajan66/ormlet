from typing import ClassVar

from models.fields.base import Field


class Model:
    _fields: ClassVar[dict[str, Field]] = {}

    """
    Runs for every model that inherits this class,
    """

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls._tablename = kwargs.get("tablename", cls.__name__.lower())
        # cls.objects = Manager() # TODO: implement objects manager

        cls._fields = {
            name: value
            for name, value in cls.__dict__.items()
            if isinstance(value, Field)
        }
