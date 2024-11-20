from apps.core.api.viewsets import BaseModelViewSet
from apps.plans.models import Subscription, Plan
from apps.plans.api.serializers import SubscriptionSerializer
from apps.payment.providers.mercadopago import MercadoPagoProvider
from apps.payment.models import PaymentMethod

from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class SubscriptionViewSet(BaseModelViewSet):
    model = Subscription
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        plan_id = request.data.get("plan")
        plan = Plan.objects.get(id=plan_id, is_active=True)
        payment_method_id = request.data.get("payment_method_id")

        if not plan:
            return Response({"error": "Plano de assinatura não encontrado"}, status=HTTP_400_BAD_REQUEST)

        if payment_method_id:
            payment_method = PaymentMethod.objects.filter(user=user, id=payment_method_id, is_active=True).first()
        else:
            payment_method = PaymentMethod.objects.filter(user=user, is_default=True, is_active=True).first()

        if not payment_method:
            return Response({"error": "Método de pagamento não encontrado"}, status=HTTP_400_BAD_REQUEST)

        service = MercadoPagoProvider()
        subscription_response = service.create_subscription(user, plan, payment_method)

        if subscription_response.get("status") == 201:
            subscription = Subscription.objects.create(
                user=user,
                plan=plan,
                status=subscription_response["response"]["status"],
                external_id=subscription_response["response"]["id"],
                next_billing_date=subscription_response["response"].get("next_payment_date"),
            )
            return Response(self.serializer_class(subscription).data)
        else:
            return Response(
                {"error": "Erro ao criar assinatura"},
                status=HTTP_400_BAD_REQUEST,
            )
