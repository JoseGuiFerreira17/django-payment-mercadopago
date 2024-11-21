from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from apps.core.api.viewsets import BaseModelViewSet
from apps.payment.api.serializers import PaymentSerializer
from apps.payment.models import Payment, PaymentMethod
from apps.core.providers.mercadopago import MercadoPagoProvider


class PaymentViewSet(BaseModelViewSet):
    model = Payment
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        payment_method_id = request.data.get("payment_method_id")

        if payment_method_id:
            payment_method = PaymentMethod.objects.filter(
                user=request.user, id=payment_method_id, is_active=True
            ).first()
        else:
            payment_method = PaymentMethod.objects.filter(user=request.user, is_default=True, is_active=True).first()

        if not payment_method:
            return Response({"error": "Método de pagamento não encontrado"}, status=HTTP_400_BAD_REQUEST)

        service = MercadoPagoProvider()
        payment_response = service.process_payment(user, request.data, payment_method)

        if payment_response["status"] == 201:
            payment_data = {
                "user": user,
                "amount": request.data.get("amount"),
                "description": request.data.get("description"),
                "installments": request.data.get("installments"),
                "status": payment_response["response"]["status"],
                "transaction_id": payment_response["response"]["id"],
            }
            payment = Payment.objects.create(**payment_data)
            return Response(self.serializer_class(payment).data)
        else:
            return Response(
                {"error": "Erro ao processar o pagamento"},
                status=HTTP_400_BAD_REQUEST,
            )
