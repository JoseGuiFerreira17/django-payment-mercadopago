from datetime import datetime, timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.accounts.models import User
from apps.core.providers.mercadopago import MercadoPagoProvider


@receiver(pre_save, sender=User)
def create_customer_mercadopago(sender, instance, **kwargs):
    if instance._state.adding:
        user = instance
        address = user.address
        service = MercadoPagoProvider()

        customer_data = {
            "email": user.email,
            "first_name": user.name.split()[0],
            "last_name": " ".join(user.name.split()[1:]),
            "phone": {
                "area_code": "55",
                "number": user.phone,
            },
            "identification": {
                "type": "CPF" if len(user.document) == 11 else "CNPJ",
                "number": user.document,
            },
            "date_registered": datetime.now(timezone.utc).isoformat(),
        }
        if address:
            customer_data["address"] = {
                "zip_code": address.zip_code,
                "street_name": address.street,
                "street_number": address.number,
                "city": {
                    "name": address.city,
                },
            }
        response = service.create_customer(customer_data)
        if response and isinstance(response, dict) and "id" in response:
            user.external_id = response["id"]
        else:
            raise ValueError("Erro ao criar cliente no Mercado Pago")
