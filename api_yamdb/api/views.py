from rest_framework import viewsets, filters, permissions
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import (GenreSerializer, 
                             TitleSerializer, 
                             СategorySerializer, 
                             ReviewSerializer,
                             CommentSerializer)
from reviews.models import Genre, Title, Сategory, Review, Comment


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Сategory.objects.all()
    serializer_class = СategorySerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)
    pagination_class = None


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter)
    search_fields = ('name',)
    pagination_class = None


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]