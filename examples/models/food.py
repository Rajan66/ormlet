import models


class Food(models.Model):
    name = models.CharField(
        max_length=50,
    )

    origin = models.CharField()

    non_veg = models.BooleanField(
        null=True,
        default=True,
    )
