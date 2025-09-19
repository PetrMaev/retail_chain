from django.urls import path

from links.apps import LinksConfig
from links.views import LinkCreateAPIView, LinkListAPIView, LinkRetrieveAPIView, LinkUpdateAPIView, LinkDestroyAPIView, LinkUpdateForBuyerAPIView

app_name = LinksConfig.name

urlpatterns = [
    path("links/create/", LinkCreateAPIView.as_view(), name="link-create"),
    path("links/", LinkListAPIView.as_view(), name="link-list"),
    path("links/<int:pk>/", LinkRetrieveAPIView.as_view(), name="link-detail"),
    path("links/<int:pk>/edit/", LinkUpdateAPIView.as_view(), name="link-edit"),
    path("links/<int:pk>/edit_buyer/", LinkUpdateForBuyerAPIView.as_view(), name="link-edit-for-buyer"),
    path("links/<int:pk>/delete/", LinkDestroyAPIView.as_view(), name="link-delete")
]
