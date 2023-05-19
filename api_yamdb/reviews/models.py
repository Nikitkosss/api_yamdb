from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Сategory(models.Model):
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Подзаголовок',
    )
    name = models.TextField(
        max_length=256,
        verbose_name='Название категории'
    )


class Genre(models.Model):
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Подзаголовок',
    )
    name = models.TextField(
        max_length=256,
        verbose_name='Название категории'
    )


class Title(models.Model):
    category = models.ForeignKey(
        Сategory,
        on_delete=models.CASCADE,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='titles',
        verbose_name='Жанр'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Название произведения'
    )
    name = models.TextField(
        max_length=256,
        verbose_name='Название произведения'
    )
    year = models.DateTimeField(
        verbose_name='Год выпуска',
    )

    def __str__(self):
        return self.name
