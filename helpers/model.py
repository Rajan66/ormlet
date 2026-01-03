from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.base import Field


class ModelHelper:
    @staticmethod
    def get_column_constraints(field, field_obj: Field) -> str:
        constraints = ""
        for key, value in field_obj.__dict__.items():
            if key is not None:
                if key == "max_length" and value:
                    constraints += f"({value}) "

                if key == "min_length" and value:
                    constraints += f"CHECK (LENGTH({field})>={value})"

                if key == "null":
                    constraints += "NULL " if value else "NOT NULL "

                if key == "unique" and value:
                    constraints += "UNIQUE "

                if key == "default" and value:
                    constraints += f"DEFAULT {value}"
        return constraints
