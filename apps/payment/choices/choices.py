from django.db.models import TextChoices


class PaymentMethodChoices(TextChoices):
    CREDIT_CARD = "credit_card", "Cartão de Crédito"
    DEBIT_CARD = "debit_card", "Cartão de Débito"
    PIX = "pix", "PIX"
