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
        on_delete=models.PROTECT,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='genre_titles',
        verbose_name='Жанр'
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    name = models.TextField(
        max_length=256,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
    )

    def __str__(self):
        return self.name
