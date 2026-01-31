from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Model


class QuerySet:
    def __init__(self, model: Model):
        self.model = model

    def get(self, *_, **kwargs):
        query = "SELECT * FROM %s"
        if kwargs:
            query += "WHERE "
            for key, value in kwargs.items():
                query += f"{key}={value}"
        query += ";"
        return query

    def all(self):
        fields = ""
        for index, field in enumerate(self.model._fields.keys()):
            if index == self.model._fields.__len__() - 1:
                fields += field
            else:
                fields += field + ", "

        query = f"SELECT {fields} FROM %s;"
        return query
