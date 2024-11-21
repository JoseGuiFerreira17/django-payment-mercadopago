from django.contrib.admin import ModelAdmin
from apps.core.providers.mercadopago import MercadoPagoProvider


class PlanAdmin(ModelAdmin):
    list_display = ("name", "price", "billing_period", "external_id", "is_active")
    list_filter = ("billing_period", "is_active")
    search_fields = ("name", "price")
    ordering = ("name", "price")
    actions = ("get_mercadopago_plans",)
    fieldsets = (
        (
            "Informações do Plano",
            {"fields": ("name", "price", "description", "billing_period", "external_id", "is_active")},
        ),
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_mercadopago_plans(self, request, queryset):
        service = MercadoPagoProvider()
        response = service.get_plans()
        if response:
            self.model.objects.all().delete()
            for plan in response:
                self.model.objects.create(
                    name=plan.get("reason"),
                    price=plan.get("auto_recurring").get("transaction_amount"),
                    billing_period=plan.get("auto_recurring").get("frequency"),
                    external_id=plan.get("id"),
                    is_active=True if plan.get("status") == "active" else False,
                )
        else:
            self.message_user(request, "Nenhum plano encontrado no Mercado Pago", "error")

    get_mercadopago_plans.short_description = "Obter planos do Mercado Pago"
