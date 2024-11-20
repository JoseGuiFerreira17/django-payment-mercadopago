import mercadopago
from django.conf import settings
from apps.accounts.models import User


class MercadoPagoProvider:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sdk = mercadopago.SDK(settings.MERCADO_PAGO_ACCESS_TOKEN)

    def process_payment(self, user, payment, payment_method):
        payment_data = {
            "transaction_amount": float(payment.get("amount")),
            "token": payment_method.card_number,
            "description": payment.get("description"),
            "installments": payment.get("installments"),
            "payment_method_id": payment_method.issuer,
            "payer": {
                "email": user.email,
                "identification": {
                    "type": "CPF",
                    "number": user.document,
                },
                "first_name": user.name.split()[0],
                "last_name": " ".join(user.name.split()[1:]),
            },
        }
        try:
            response = self.sdk.payment().create(payment_data)
        except Exception as e:
            raise e
        return response

    def create_subscription(self, user, plan, payment_method):
        payload = {
            "preapproval_plan_id": plan.external_id,
            "payer_email": user.email,
            "card_token_id": payment_method.card_token,
            "auto_recurring": {
                "frequency": plan.billing_cycle,
                "frequency_type": "months",
                "transaction_amount": float(plan.price),
                "currency_id": "BRL",
            },
            "back_url": "https://example.com/subscription-success",
        }
        response = self._make_request("POST", "/v1/preapproval", data=payload)
        return response

    def generate_card_token(self, card_data):
        try:
            token_response = self.sdk.card_token().create(card_data)

            if token_response["status"] == 201:
                return token_response["response"]["id"]
            else:
                raise Exception(f"Erro ao gerar token: {token_response}")
        except Exception as e:
            raise Exception(f"Erro na tokenização do cartão: {e}")
