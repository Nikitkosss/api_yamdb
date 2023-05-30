from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
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
        Category,
        on_delete=models.CASCADE,
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


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва')
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение')
    text = models.TextField(
        verbose_name='Текст отзыва')
    score = models.IntegerField(
        verbose_name='Оценка произведения')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата отзыва')

    class Meta:
        ordering = ['pub_date', ]
        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='constraint_author_title'
            ),
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария')
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв')
    text = models.TextField(
        verbose_name='Текст комментария')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата комментария')

    class Meta:
        ordering = ['pub_date', ]

    def __str__(self):
        return self.text
