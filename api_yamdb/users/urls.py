from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, create_user, create_token

v1_router = routers.DefaultRouter()
v1_router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', create_user, name='create_user'),
    path('v1/auth/token/', create_token, name='create_token'),
    path('v1/', include(v1_router.urls)),
]
