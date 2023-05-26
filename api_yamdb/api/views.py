from api.serializers import (CommentSerializer, GenreSerializer,
                             ReviewSerializer, TitleSerializer,
                             СategorySerializer, TitleSerializerForCreate)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from reviews.models import Comment, Genre, Review, Title, Сategory
from users.permissions import (ListOrAdminModeratOnly,
                               AuthenticatedPrivilegedUsersOrReadOnly)
from api.mixins import CreateListDestroyViewSet


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Сategory.objects.all()
    serializer_class = СategorySerializer
    permission_classes = (ListOrAdminModeratOnly,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)
    lookup_field = 'slug'


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (ListOrAdminModeratOnly,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (ListOrAdminModeratOnly,)
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('category', 'genre', 'name', 'year')

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return TitleSerializerForCreate
        return TitleSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author')
    permission_classes = [AuthenticatedPrivilegedUsersOrReadOnly, ]


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author')
    permission_classes = [AuthenticatedPrivilegedUsersOrReadOnly, ]
