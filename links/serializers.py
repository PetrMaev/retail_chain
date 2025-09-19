from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Link
        fields = "__all__"


class LinkSerializerForBuyer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Link
        fields = [
            "title",
            "email",
            "owner",
            "country",
            "city",
            "street",
            "house_number",
            "product_name",
            "product_model",
            "realize_date",
            "provider",
            "network_level",
            "debt",
            "created_at"
        ]
        extra_kwargs = {
            "debt": {"read_only": True},
            "network_level": {"read_only": True}
        }
