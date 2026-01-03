from typing import TYPE_CHECKING

import examples.models as model_classes
from commands.base import Command

if TYPE_CHECKING:
    from models.base import Model

model_list: dict[str, Model] = {
    name: getattr(model_classes, name) for name in model_classes.__all__
}


class ListModelCommand(Command):
    name = "listmodel"

    def run(self):
        [
            print(f"{index + 1}. {model_name}")
            for index, model_name in enumerate(model_list.keys())
        ]
