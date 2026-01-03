import logging
from typing import TYPE_CHECKING

import examples.models as model_classes
from commands.base import Command
from managers.db import ModelManager

if TYPE_CHECKING:
    from models import Model

model_list: dict[str, Model] = {
    name: getattr(model_classes, name) for name in model_classes.__all__
}


class MigrateCommand(Command):
    name = "migrate"

    def run(self):
        for model_name, model in model_list.items():
            try:
                ModelManager.create_table(
                    model._tablename,
                    model._fields,
                )
                logging.info(f"{model_name} migrated successfully")
            except Exception as ex:
                logging.info(f"Failed to migrate {model_name}: {ex}")
                raise
        return
