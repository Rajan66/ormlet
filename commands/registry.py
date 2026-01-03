from typing import TYPE_CHECKING, Dict, Optional, Type

if TYPE_CHECKING:
    from .base import Command


class CommandRegistry:
    def __init__(self) -> None:
        self._commands: Dict[str, Type[Command]] = {}

    def register(self, command_cls: Type[Command]) -> None:
        self._commands[command_cls.name] = command_cls

    def get(self, name: str) -> Optional[Type[Command]]:
        return self._commands.get(name)

    def all(self) -> list[str]:
        return list(self._commands.keys())
