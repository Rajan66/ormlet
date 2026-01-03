import models
from models.base import Model


class User(Model):
    email = models.CharField(
        unique=True,
    )

    name = models.CharField()

    age = models.IntegerField(
        null=True,
    )

    is_active = models.BooleanField()
