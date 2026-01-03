from models.fields.base import Field


class CharField(Field):
    def get_internal_type(self):
        return "CharField"
