import models
from models.base import Model


class User(Model):
    email = models.CharField(
        unique=True,
        null=False,
    )

    name = models.CharField(
        min_length=3,
        max_length=10,
    )

    age = models.IntegerField(
        null=True,
    )

    is_active = models.BooleanField(
        null=False,
        default=True,
    )
