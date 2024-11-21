from django.contrib.admin import ModelAdmin


class PaymentMethodAdmin(ModelAdmin):
    list_display = ["user", "payment_type", "card_holder_name", "card_number", "is_active", "is_default"]
    search_fields = ["user__name", "user__email", "payment_type", "card_holder_name"]
    ordering = ["-created_at"]

    fieldsets = [
        (
            "Informações do método de pagamento",
            {
                "fields": [
                    "user",
                    "payment_type",
                    "card_holder_name",
                    "card_number",
                    "last_four_digits",
                    "expiration_month",
                    "expiration_year",
                    "security_code",
                    "issuer",
                    "is_active",
                    "is_default",
                ]
            },
        )
    ]
