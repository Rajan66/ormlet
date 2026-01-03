from models.base import Model


class ModelHelper:
    @staticmethod
    def get_model_fields(model_class: Model):
        pass
        # fields = model_class.fields.copy()
        # for key, value in fields.items():
        #     fields[key] = type(value).__name__
        # return fields
