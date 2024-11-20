from django.db.models import CharField, ForeignKey, CASCADE, PROTECT, DateField
from apps.core.models import BaseModelMixin
from apps.plans.choices import PlanStatus


class Subscription(BaseModelMixin):
    user = ForeignKey("accounts.User", verbose_name="usuário", on_delete=CASCADE, related_name="subscriptions")
    plan = ForeignKey("plans.Plan", verbose_name="plano", on_delete=PROTECT, related_name="subscriptions")
    external_id = CharField(verbose_name="ID externo do mercado pago", max_length=255, null=True, blank=True)
    status = CharField(verbose_name="status", max_length=255, choices=PlanStatus.choices, default=PlanStatus.PENDING)
    next_billing_date = DateField(verbose_name="próxima data de cobrança", null=True, blank=True)

    class Meta:
        verbose_name = "assinatura"
        verbose_name_plural = "assinaturas"

    def __str__(self):
        return f"{self.user} - {self.plan}"
