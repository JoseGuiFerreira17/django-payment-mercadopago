from apps.core.api.viewsets import BaseReadOnlyModelViewSet
from apps.plans.models import Plan
from apps.plans.api.serializers import PlanSerializer


class PlanViewSet(BaseReadOnlyModelViewSet):
    model = Plan
    serializer_class = PlanSerializer
