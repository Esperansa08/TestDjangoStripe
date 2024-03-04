from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название предмета",
    )
    description = models.TextField(
        max_length=200,
        verbose_name="описание предмета")
    price = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
        help_text="Цена предмета",
    )

    class Meta:
        verbose_name_plural = "Предмет"
        verbose_name = "Предмет"

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
