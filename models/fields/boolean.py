from models.fields.base import Field


class BooleanField(Field):
    def get_internal_type(self):
        return "BooleanField"
