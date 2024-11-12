from django.db.models import CharField, PositiveIntegerField
from apps.core.models.mixin import BaseModelMixin


class Address(BaseModelMixin):
    street = CharField(max_length=255, verbose_name="rua")
    number = PositiveIntegerField(verbose_name="número", blank=True, null=True)
    complement = CharField(max_length=255, verbose_name="complemento", blank=True, null=True)
    district = CharField(max_length=255, verbose_name="bairro")
    city = CharField(max_length=255, verbose_name="cidade")
    state = CharField(max_length=2, verbose_name="estado")
    zip_code = CharField(max_length=8, verbose_name="CEP")

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
        ordering = ["street"]

    def __str__(self):
        return self.street
