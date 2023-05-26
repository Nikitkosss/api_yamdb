import datetime as dt

from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework import serializers
from reviews.models import Comment, Genre, Review, Title, Сategory

User = get_user_model()


class СategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Сategory


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True,)
    category = СategorySerializer()

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializerForCreate(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all(),
        required=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Сategory.objects.all(),
        required=True
    )

    raiting = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Title

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год релиза!')
        return value

    def get_raiting(self, object):
        return Review.objects.filter(
            title=object.id
        ).aggregate(rating=Avg("score"))['rating']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('author', 'title')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
