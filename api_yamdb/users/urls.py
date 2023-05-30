from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, create_token, create_user

router = DefaultRouter()
router.register('users', UserViewSet)

auth_urlpatterns = [
    path('token/', create_token),
    path('signup/', create_user),
]


urlpatterns = [
    path('v1/auth/', include(auth_urlpatterns)),
    path('v1/', include(router.urls)),
]
