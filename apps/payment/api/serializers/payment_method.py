from rest_framework.serializers import ModelSerializer, ValidationError
from apps.payment.models import PaymentMethod
from apps.core.providers.mercadopago import MercadoPagoProvider


class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
        }

    def create(self, validated_data):
        card_number = validated_data.pop("card_number")
        last_four_digits = card_number[-4:]
        user = self.context["request"].user

        card_data = {
            "card_number": card_number,
            "expiration_month": validated_data.get("expiration_month"),
            "expiration_year": validated_data.get("expiration_year"),
            "security_code": validated_data.get("security_code"),
            "cardholder": {
                "name": validated_data.get("card_holder_name"),
                "identification": {
                    "type": "CPF",
                    "number": user.document,
                },
            },
        }

        service = MercadoPagoProvider()
        response = service.generate_card_token(card_data)

        if response and isinstance(response, dict) and "id" in response:
            token = response.get("id")
            validated_data["card_number"] = token
            validated_data["last_four_digits"] = last_four_digits
            validated_data["user"] = self.context["request"].user

            token_data = {
                "token": token,
            }

            response = service.create_card(user.external_id, token_data)
            if response and isinstance(response, dict) and "id" in response:
                validated_data["external_id"] = response.get("id")
            else:
                raise ValidationError("Erro ao salvar o cartão.")

            return super().create(validated_data)
        else:
            raise ValidationError("Erro ao tokenizar o cartão.")
