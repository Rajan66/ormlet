from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract base class for CLI commands.

    Subclasses set ``name`` and implement ``run()``; they are registered in
    CommandRegistry.
    """
    name: str = ""

    @abstractmethod
    def run(self) -> None:
        """Execute the command. Must be implemented by subclasses."""
        ...
