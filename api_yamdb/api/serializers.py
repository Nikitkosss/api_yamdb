from rest_framework import serializers

from reviews.models import Genre, Title, User, Сategory


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
    class Meta:
        fields = '__all__'
        model = Title
