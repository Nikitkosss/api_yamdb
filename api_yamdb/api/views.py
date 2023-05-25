from api.serializers import (CommentSerializer, GenreSerializer,
                             ReviewSerializer, TitleSerializer, 
                             СategorySerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from reviews.models import Comment, Genre, Review, Title, Сategory
from users.permissions import (ListOrAdminModeratOnly,
                               AuthenticatedPrivilegedUsersOrReadOnly)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Сategory.objects.all()
    serializer_class = СategorySerializer
    permission_classes = (ListOrAdminModeratOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = None


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (ListOrAdminModeratOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = None


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (ListOrAdminModeratOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author')
    permission_classes = [AuthenticatedPrivilegedUsersOrReadOnly,]
    

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author')
    permission_classes = [AuthenticatedPrivilegedUsersOrReadOnly,]
