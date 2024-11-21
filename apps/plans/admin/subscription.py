from django.contrib.admin import ModelAdmin


class SubscriptionAdmin(ModelAdmin):
    list_display = ("plan", "user", "status", "next_billing_date")
    list_filter = ("status", "plan__name")
    search_fields = ("plan__name", "user__name")
    ordering = ("-created_at",)
    fieldsets = (
        (
            "Informações da Assinatura",
            {"fields": ("plan", "user", "status", "external_id", "next_billing_date")},
        ),
    )
