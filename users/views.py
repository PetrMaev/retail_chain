from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from links.paginators import CustomPagination
from users.models import CustomUser
from users.permissions import IsUserOwner
from users.serializers import UserCreateSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserCreateSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsUserOwner]
