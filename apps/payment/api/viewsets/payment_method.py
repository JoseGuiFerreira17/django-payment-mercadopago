from apps.core.api.viewsets import BaseModelViewSet
from apps.payment.api.serializers import PaymentMethodSerializer
from apps.payment.models import PaymentMethod


class PaymentMethodViewSet(BaseModelViewSet):
    model = PaymentMethod
    serializer_class = PaymentMethodSerializer
