from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import CustomUser


class Link(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название звена торговой сети",
        help_text="Укажите название звена торговой сети"
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        help_text="Укажите электронную почту"
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец звена торговой сети"
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Страна",
        help_text="Укажите страну",
    )
    city = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите город",
    )
    street = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Улица",
        help_text="Укажите улицу",
    )
    house_number = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Номер дома",
        help_text="Укажите номер дома",
    )
    product_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Название продукта",
        help_text="Укажите название продукта",
    )
    product_model = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Модель продукта",
        help_text="Укажите модель продукта",
    )
    realize_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата выхода продукта на рынок",
        help_text="Укажите дату выхода продукта на рынок",
    )
    provider = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Поставщик",
        help_text="Укажите поставщика",
    )
    network_level = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0, message="Уровень сети не может быть меньше 0"),
            MaxValueValidator(2, message="Уровень сети не может быть больше 2"),
        ],
        default=None,
        blank=True,
        null=True,
        verbose_name="Уровень сети",
    )
    debt = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Задолженность перед поставщиком",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
