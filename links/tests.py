from datetime import datetime
from unittest.mock import patch

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from links.models import Link
from users.models import CustomUser


class LinkTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            email="tester@sky.pro"
        )

        self.link = Link.objects.create(
            title="Samsung",
            email="samsung@gmail.com",
            owner=self.user,
            country="South Korea",
            city="Suwon",
            product_name="Smartphone",
            product_model="Galaxy S25 Ultra",
            realize_date="2025-02-07",
            network_level=0,
            debt=0.00,
            created_at="2025-09-19 17:00:00",
        )
        self.client.force_authenticate(user=self.user)

    def test_link_retrieve(self):
        """Тестирование просмотра звена сети."""

        url = reverse("links:link-detail", args=(self.link.pk,))

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.link.title)

    def test_link_create(self):
        """Тестирование создания звена сети."""

        url = reverse("links:link-create")
        data = {
            "owner": self.user,
            "title": "Apple",
            "email": "apple@icloud.com",
            "country": "USA",
            "city": "Cupertino",
            "product_name": "Smartphone",
            "product_model": "Iphone 17",
            "realize_date": "2025-09-09",
            "network_level": 0,
            "created_at": "2025-09-19 17:00:00",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Link.objects.all().count(), 2)

    def test_link_update(self):
        """Тестирование изменения звена сети."""

        url = reverse("links:link-edit", args=(self.link.pk,))

        data = {
            "product_model": "Iphone 17 Pro Max 1 TB",
        }

        response = self.client.patch(url, data)
        self.assertEqual(data.get("product_model"), "Iphone 17 Pro Max 1 TB")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_link_delete(self):
        """Тестирование удаления звена сети"""

        url = reverse("links:link-delete", args=(self.link.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Link.objects.all().count(), 0)

    def test_link_list(self):
        """Тестирование вывода списка курсов."""

        url = reverse("links:link-list")
        self.fixed_time = timezone.make_aware(datetime(2025, 9, 19, 17, 0))
        with patch("django.db.models.DateTimeField", auto_now_add=False):
            self.link = Link.objects.update(created_at=self.fixed_time)
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "owner": self.user.pk,
                    "title": "Samsung",
                    "email": "samsung@gmail.com",
                    "country": "South Korea",
                    "city": "Suwon",
                    "street": None,
                    "house_number": None,
                    "product_name": "Smartphone",
                    "product_model": "Galaxy S25 Ultra",
                    "realize_date": "2025-02-07",
                    "network_level": 0,
                    "debt": "0.00",
                    "provider": None,
                    "created_at": self.fixed_time.strftime("%Y-%m-%d %H:%M:%S"),
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
