import datetime as dt

from rest_framework import serializers
from reviews.models import Genre, Title, User, Сategory, Comment, Review



class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Имя пользователя не может быть "me".'
            )
        return username


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class СategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Сategory


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all(),
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

    class Meta:
        model = Review
        fields =('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('author', 'title')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    commenting = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
