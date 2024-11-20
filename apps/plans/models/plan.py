from django.db.models import CharField, DecimalField, IntegerField, BooleanField
from apps.core.models import BaseModelMixin


class Plan(BaseModelMixin):
    name = CharField(verbose_name="nome", max_length=255)
    description = CharField(verbose_name="descrição", max_length=255, null=True, blank=True)
    price = DecimalField(verbose_name="preço", max_digits=10, decimal_places=2)
    billing_period = IntegerField(verbose_name="período de cobrança em meses", default=1)
    is_active = BooleanField(verbose_name="ativo", default=True)

    class Meta:
        verbose_name = "plano"
        verbose_name_plural = "planos"

    def __str__(self):
        return self.name
