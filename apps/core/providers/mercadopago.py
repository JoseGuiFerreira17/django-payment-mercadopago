import mercadopago
from django.conf import settings
from datetime import datetime, timedelta


class MercadoPagoProvider:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.access_token = settings.MERCADO_PAGO_ACCESS_TOKEN
        self.sdk = mercadopago.SDK(self.access_token)

    def get_plans(self):
        try:
            response = self.sdk.plan().search()
            if response["status"] == 200:
                results = response.get("response").get("results", [])
                return results
            else:
                raise Exception(f"Erro ao buscar planos: {response}")
        except Exception as e:
            raise Exception(f"Erro ao buscar planos: {e}")

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
        start_date = datetime.utcnow()
        end_date = start_date + timedelta(days=30)
        if plan.billing_period > 1:
            end_date = start_date + timedelta(days=30 * plan.billing_period)

        start_date_iso = start_date.isoformat() + "Z"
        end_date_iso = end_date.isoformat() + "Z"

        payload = {
            "preapproval_plan_id": plan.external_id,
            "payer_email": user.email,
            "card_token_id": payment_method.card_number,
            "auto_recurring": {
                "frequency": plan.billing_period,
                "frequency_type": "months",
                "start_date": start_date_iso,
                "end_date": end_date_iso,
                "transaction_amount": float(plan.price),
                "currency_id": "BRL",
            },
            "back_url": "https://example.com/subscription-success",
        }
        response = self.sdk.subscription().create(payload)
        return response

    def create_customer(self, customer_data):
        try:
            response = self.sdk.customer().create(customer_data)
            if response["status"] == 201:
                return response["response"]
            else:
                raise Exception(f"Erro ao criar cliente: {response}")
        except Exception as e:
            raise Exception(f"Erro ao criar cliente: {e}")

    def create_card(self, customer, card_token):
        try:
            response = self.sdk.card().create(customer, card_token)
            if response["status"] == 201:
                return response["response"]
            else:
                raise Exception(f"Erro ao criar cartão: {response}")
        except Exception as e:
            raise Exception(f"Erro ao criar cartão: {e}")

    def generate_card_token(self, card_data):
        try:
            token_response = self.sdk.card_token().create(card_data)

            if token_response["status"] == 201:
                return token_response["response"]
            else:
                raise Exception(f"Erro ao gerar token: {token_response}")
        except Exception as e:
            raise Exception(f"Erro na tokenização do cartão: {e}")
