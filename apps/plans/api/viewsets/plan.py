from apps.core.api.viewsets import BaseModelViewSet
from apps.plans.models import Plan
from apps.plans.api.serializers import PlanSerializer


class PlanViewSet(BaseModelViewSet):
    model = Plan
    serializer_class = PlanSerializer
