from models.base import Model


class User(Model):
    # TODO: change the datatype into separate classes
    fields = {
        "email": "",
        "name": "",
        "age": 0,
        "is_active": False,
    }
