import datetime as dt

from django.contrib.auth import get_user_model
from rest_framework import serializers
from reviews.models import Comment, Genre, Review, Title, Category

User = get_user_model()
MAXSIMUMRATING = 10


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True,)
    category = CategorySerializer()

    class Meta:
        fields = '__all__'
        model = Title

    rating = serializers.FloatField()


class TitleSerializerForCreate(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all(),
        required=True
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=True
    )

    class Meta:
        fields = '__all__'
        model = Title

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год релиза!')
        return value


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    def validate(self, data):

        if data['score'] > MAXSIMUMRATING:
            raise serializers.ValidationError(f'Максимальная оценка - {MAXSIMUMRATING} !')
        return data
            

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('author', 'title')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('author', 'title' ), 
                message=("Some custom message."))
        ]



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
