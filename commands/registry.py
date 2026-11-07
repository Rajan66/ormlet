from typing import TYPE_CHECKING, Dict, Optional, Type

if TYPE_CHECKING:
    from .base import Command


class CommandRegistry:
    """Registry mapping command names to Command classes."""

    def __init__(self) -> None:
        self._commands: Dict[str, Type[Command]] = {}

    def register(self, command_cls: Type[Command]) -> None:
        """Register command_cls under its ``name`` attribute."""
        self._commands[command_cls.name] = command_cls

    def get(self, name: str) -> Optional[Type[Command]]:
        """Look up a command class by name; return None if not registered."""
        return self._commands.get(name)

    def all(self) -> list[str]:
        """Return the names of every registered command."""
        return list(self._commands.keys())
