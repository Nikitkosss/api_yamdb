from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import (GenreSerializer, TitleSerializer,
                             СategorySerializer)
from reviews.models import Genre, Title, Сategory


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Сategory.objects.all()
    serializer_class = СategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = None


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = None


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')
