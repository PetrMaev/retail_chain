from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter

from links.models import Link
from links.paginators import CustomPagination
from links.permissions import IsFactory
from links.serializers import LinkSerializer, LinkSerializerForBuyer
from users.permissions import IsUserActive


class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsUserActive]

    def perform_create(self, serializer):
        task = serializer.save(owner=self.request.user)  # noqa: F841


class LinkListAPIView(generics.ListAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsUserActive]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["id", "title", "email", "country"]
    ordering_fields = ["id", "country", "email", "title"]
    filterset_fields = ["country", "network_level"]


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsUserActive]


class LinkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsUserActive, IsFactory]


class LinkUpdateForBuyerAPIView(generics.UpdateAPIView):
    serializer_class = LinkSerializerForBuyer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsUserActive]


class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsUserActive]
