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
    preference_id = CharField(
        verbose_name="id preferência", max_length=255, blank=True, null=True
    )
    description = CharField(verbose_name="descrição", max_length=255)
    total = DecimalField(verbose_name="total", max_digits=10, decimal_places=2)
    currency = CharField(verbose_name="moeda", max_length=10, default="BRL")
    quantity = IntegerField(verbose_name="quantidade", default=1)
    status = CharField(verbose_name="status", max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.preference_id} - {self.description}"
