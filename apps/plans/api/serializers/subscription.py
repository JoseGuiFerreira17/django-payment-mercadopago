from rest_framework.serializers import ModelSerializer, CharField
from apps.plans.models import Subscription


class SubscriptionSerializer(ModelSerializer):
    payment_method_id = CharField(write_only=True, required=False)

    class Meta:
        model = Subscription
        fields = "__all__"
        extra_kwargs = {
            "user": {"required": False},
        }
