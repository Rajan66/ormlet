from typing import ClassVar

from managers import Manager
from models.fields.base import Field


class Model:
    """Base ORM model.

    Uses __init_subclass__ to register each subclass: sets _tablename, binds a
    Manager as objects, and collects Field class attributes into _fields.
    """

    _fields: ClassVar[dict[str, Field]] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        """Set _tablename, bind Manager(cls) as objects,
        collect Field instances.
        """
        super().__init_subclass__(**kwargs)
        cls._tablename = kwargs.get("tablename", cls.__name__.lower())
        cls.objects = Manager(cls)

        cls._fields = {
            name: value
            for name, value in cls.__dict__.items()
            if isinstance(value, Field)
        }
