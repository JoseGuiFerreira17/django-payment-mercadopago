from django.db.models import TextChoices
from django.utils.translation import pgettext_lazy


class PaymentMethodChoices(TextChoices):
    CREDIT_CARD = "credit_card", "Cartão de Crédito"
    DEBIT_CARD = "debit_card", "Cartão de Débito"
    PIX = "pix", "PIX"


class PaymentStatus(TextChoices):
    WAITING = "waiting", "Aguardando"
    PREAUTH = "preauth", "Pré Autorizado"
    CONFIRMED = "confirmed", "Confirmado"
    REJECTED = "rejected", "Rejeitado"
    REFUNDED = "refunded", "Estornado"
    ERROR = "error", "Erro"
    INPUT = "input", "Aguardando Entrada"
