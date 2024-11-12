from rest_framework.serializers import ModelSerializer

from apps.core.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "created_at",
            "modified_at",
            "street",
            "number",
            "complement",
            "district",
            "city",
            "state",
            "zip_code",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }
