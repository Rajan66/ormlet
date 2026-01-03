from abc import ABC, abstractmethod


class Command(ABC):
    name: str = ""

    @abstractmethod
    def run(self) -> None: ...
