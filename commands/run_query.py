from commands.base import Command
from examples.query import RetrieveQueryService


class RunQueryCommand(Command):
    """Run the example RetrieveQueryService (queries Food and prints rows)."""

    name = "run-query"

    def run(self):
        RetrieveQueryService().start()
