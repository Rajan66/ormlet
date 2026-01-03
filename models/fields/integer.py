from models.fields.base import Field


class IntegerField(Field):
    def get_internal_type(self):
        return "IntegerField"
