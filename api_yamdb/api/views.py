from rest_framework import viewsets

from api.serializers import (GenreSerializer, TitleSerializer,
                             СategorySerializer)
from reviews.models import Genre, Title, Сategory


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Сategory.objects.all()
    serializer_class = СategorySerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
