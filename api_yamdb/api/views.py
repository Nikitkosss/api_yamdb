from api.mixins import CreateListDestroyViewSet
from api.serializers import (CommentSerializer, GenreSerializer,
                             ReviewSerializer, TitleSerializer,
                             TitleSerializerForCreate, CategorySerializer)
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from reviews.models import Comment, Genre, Review, Title, Category
from users.permissions import (AuthenticatedPrivilegedUsersOrReadOnly,
                               ListOrAdminModeratOnly)
from .filters import FilterTitle
from django.db.models import Avg


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
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
    filterset_class = FilterTitle

    def get_queryset(self):
        return Title.objects.annotate(rating=Avg('reviews__score'))

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitleSerializerForCreate
        return TitleSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('text', 'author', 'title')
    permission_classes = [AuthenticatedPrivilegedUsersOrReadOnly, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method in ['POST', ]:
            context["title_id"] = self.kwargs['title_id']
            context["user_id"] = self.request.user
            return context
        return context

    def get_queryset(self):
        if self.kwargs.get('review_id'):
            return Review.objects.filter(pk=self.kwargs.get('review_id'))
        return Review.objects.filter(title=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [AuthenticatedPrivilegedUsersOrReadOnly, ]

    def get_queryset(self):
        if self.kwargs.get('comment_id'):
            return Comment.objects.filter(pk=self.kwargs.get('comment_id'))

        return Comment.objects.filter(review=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, review=review)

    def perform_update(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, review=review)
