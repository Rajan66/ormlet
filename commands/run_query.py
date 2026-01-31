from commands.base import Command
from examples.query import RetrieveQueryService


class RunQueryCommand(Command):
    name = "run-query"

    def run(self):
        RetrieveQueryService().start()
