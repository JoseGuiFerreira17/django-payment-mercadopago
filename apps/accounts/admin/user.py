from django.contrib.auth.admin import UserAdmin as DJUserAdmin


class UserAdmin(DJUserAdmin):
    list_display = [
        "name",
        "email",
        "document",
        "phone",
        "birth_date",
        "is_active",
    ]
    list_filter = ["is_staff", "is_active", "is_superuser"]
    ordering = ["-created_at"]
    fieldsets = [
        [
            "Informações pessoais",
            {"fields": ["name", "email", "document", "phone", "birth_date", "address"]},
        ],
        [
            "Dados de acesso",
            {"fields": ["password", "is_staff", "is_active", "is_superuser"]},
        ],
    ]
    add_fieldsets = [
        [
            "Informações pessoais",
            {"fields": ["name", "email", "document", "phone", "birth_date", "address"]},
        ],
        [
            "Dados de acesso",
            {"fields": ["password1", "password2", "is_staff", "is_active", "is_superuser"]},
        ],
    ]
    search_fields = ["name", "email"]
    filter_horizontal = []
