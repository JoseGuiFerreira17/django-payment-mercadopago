from apps.core.api.viewsets import BaseModelViewSet
from apps.payment.api.serializers import PaymentSerializer
from apps.payment.models import Payment


class PaymentViewSet(BaseModelViewSet):
    model = Payment
    serializer_class = PaymentSerializer
