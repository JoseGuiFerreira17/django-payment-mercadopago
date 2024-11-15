from rest_framework.serializers import ModelSerializer, UUIDField
from apps.payment.models import Payment


class PaymentSerializer(ModelSerializer):
    payment_method_id = UUIDField(required=False)

    class Meta:
        model = Payment
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "variant": {"required": False},
        }

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["variant"] = "default"
        return super().create(validated_data)
