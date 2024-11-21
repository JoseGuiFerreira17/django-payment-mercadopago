from django.contrib.admin import ModelAdmin


class PaymentAdmin(ModelAdmin):
    list_display = ["user", "amount", "installments", "status"]
    search_fields = ["user__name", "user__email", "amount", "status"]
    ordering = ["-created_at"]

    fieldsets = [
        (
            "Informações do pagamento",
            {
                "fields": [
                    "user",
                    "amount",
                    "installments",
                    "description",
                    "transaction_id",
                    "status",
                ]
            },
        )
    ]
