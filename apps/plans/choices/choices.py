from django.db.models import TextChoices


class PlanStatus(TextChoices):
    AUTHORIZED = "authorized", "Autorizado"
    PENDING = "pending", "Pendente"
