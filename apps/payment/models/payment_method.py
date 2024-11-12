from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    DateField,
    BooleanField,
)
from apps.core.models import BaseModelMixin
from apps.payment.choices import PaymentMethodChoices


class PaymentMethod(BaseModelMixin):

    user = ForeignKey(
        "accounts.user",
        verbose_name="Usuário",
        on_delete=CASCADE,
        related_name="payment_methods",
    )
    payment_type = CharField(
        verbose_name="Tipo de pagamento",
        max_length=50,
        choices=PaymentMethodChoices.choices,
    )
    last_four_digits = CharField(
        verbose_name="Últimos quatro dígitos", max_length=4, blank=True, null=True
    )
    expiration_date = DateField(
        verbose_name="Data de vencimento", blank=True, null=True
    )
    provider = CharField(verbose_name="Provedor", max_length=100, blank=True, null=True)
    is_active = BooleanField(verbose_name="Ativo", default=True)

    def __str__(self):
        return f"{self.get_payment_type_display()} - {self.user.username}"
