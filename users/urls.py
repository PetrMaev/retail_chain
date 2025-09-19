from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("users/register/", UserCreateAPIView.as_view(), name="user-register"),
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-detail"),
    path("users/<int:pk>/edit/", UserUpdateAPIView.as_view(), name="user-edit"),
    path("users/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
