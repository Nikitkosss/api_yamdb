from api.serializers import (GenreSerializer, SignUpSerializer,
                             TitleSerializer, TokenSerializer,
                             СategorySerializer)
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from reviews.models import Genre, Title, User, Сategory


def send_confirmation_code(username):
    """Функция для отправки email на почту."""
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    yamdb_email = 'yamdb@gmail.com'
    send_mail(
        'Код для регистрации',
        f'Код: {confirmation_code}',
        yamdb_email,
        [user.email],
        fail_silently=False,
    )
    user.save()


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    """ApiView-функция для регистрации."""
    username = request.data.get('username')
    email = request.data.get('email')
    if User.objects.filter(username=username, email=email).exists():
        user = get_object_or_404(User, username=username)
        serializer = SignUpSerializer(user, data=request.data)
        if serializer.is_valid():
            send_confirmation_code(username)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_confirmation_code(username)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    """ApiView-функция для получения токена."""
    serializer = TokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    username = serializer.validated_data.get('username')
    confirmation_code = serializer.validated_data.get('confirmation_code')
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, str(confirmation_code)):
        token_data = {'token': str(AccessToken.for_user(user))}
        return Response(token_data,
                        status=status.HTTP_200_OK)
    return Response('Код подтверждения неверный',
                    status=status.HTTP_400_BAD_REQUEST)


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
