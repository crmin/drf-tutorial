from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from snippets import views

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', obtain_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
    path('auth/verify/', verify_jwt_token),
    path('', include(router.urls)),
]
