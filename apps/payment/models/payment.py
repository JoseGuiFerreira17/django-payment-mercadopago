from django.db.models import (
    CharField,
    ForeignKey,
    CASCADE,
    DecimalField,
    IntegerField,
)
from apps.core.models import BaseModelMixin


class Payment(BaseModelMixin):
    user = ForeignKey(
        "accounts.User",
        verbose_name="usuário",
        on_delete=CASCADE,
        related_name="payments",
    )
    amount = DecimalField(verbose_name="valor", max_digits=10, decimal_places=2)
    installments = IntegerField(verbose_name="parcelas", default=1)
    description = CharField(verbose_name="descrição", max_length=255, null=True, blank=True)
    transaction_id = CharField(verbose_name="ID da transação", max_length=255, blank=True, null=True)
    status = CharField(verbose_name="status", max_length=255, blank=True, null=True)
