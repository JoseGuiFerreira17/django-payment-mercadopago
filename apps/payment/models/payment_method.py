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
    card_holder_name = CharField(verbose_name="Nome do titular", max_length=100, blank=True, null=True)
    card_number = CharField(verbose_name="Últimos quatro dígitos", max_length=150, blank=True, null=True)
    last_four_digits = CharField(verbose_name="Últimos quatro dígitos", max_length=4, blank=True, null=True)
    expiration_month = CharField(verbose_name="Mês de expiração", max_length=2, blank=True, null=True)
    expiration_year = CharField(verbose_name="Ano de expiração", max_length=4, blank=True, null=True)
    security_code = CharField(verbose_name="Código de segurança", max_length=4, blank=True, null=True)
    issuer = CharField(verbose_name="Bandeira", max_length=50, blank=True, null=True)
    external_id = CharField(verbose_name="ID externo mercadopago", max_length=150, blank=True, null=True)
    is_active = BooleanField(verbose_name="Ativo", default=True)
    is_default = BooleanField(verbose_name="Padrão", default=False)

    class Meta:
        verbose_name = "Método de pagamento"
        verbose_name_plural = "Métodos de pagamento"

    def save(self, *args, **kwargs):
        if self.is_default:
            PaymentMethod.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_payment_type_display()} - {self.user.name}"
