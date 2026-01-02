class ModelHelper:
    @staticmethod
    def get_model_name(model_class):
        return model_class.__name__.lower()

    @staticmethod
    def get_model_fields(model_class):
        fields = model_class.fields.copy()
        for key, _ in fields.items():
            fields[key] = type(key)
        return fields
