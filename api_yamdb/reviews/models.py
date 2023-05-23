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
        max_length=100,
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
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория'
    )
    genre = models.ForeignKey(
        Genre,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Жанр'
    )
    description = models.TextField(
        max_length=500,
        verbose_name='Описание'
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


class Review(models.Model):
    # автор отзыва
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    # произведение для отзыва
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    # текст отзыва
    text = models.TextField()
    # баллы/оценка в отзыве
    score = models.IntegerField()
    # дата отзыва
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)


class Comment(models.Model):
    # автор комментария
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    # отзыв для комментария
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    # текст комментария
    text = models.TextField()
    # дата комментария
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)    