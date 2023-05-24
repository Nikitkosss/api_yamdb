from api.views import (CategoriesViewSet, GenresViewSet, TitlesViewSet,
                       get_token, signup)
from django.urls import include, path
from rest_framework import routers

v1_router = routers.DefaultRouter()
v1_router.register('categories', CategoriesViewSet)
v1_router.register('genres', GenresViewSet)
v1_router.register('titles', TitlesViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', get_token, name='token'),
]
