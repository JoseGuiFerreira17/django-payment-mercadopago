from rest_framework.serializers import ModelSerializer
from apps.plans.models import Plan


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"
