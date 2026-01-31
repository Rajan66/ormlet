import argparse

from dotenv import load_dotenv

from commands.migrate import MigrateCommand
from commands.model_list import ListModelCommand
from commands.registry import CommandRegistry
from commands.run_query import RunQueryCommand
from setup import setup_app

load_dotenv()


def main():
    setup_app()

    registry = CommandRegistry()
    registry.register(ListModelCommand)
    registry.register(MigrateCommand)
    registry.register(RunQueryCommand)

    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=registry.all())

    args = parser.parse_args()

    command_cls = registry.get(args.command)

    if command_cls:
        command_cls().run()


if __name__ == "__main__":
    main()
