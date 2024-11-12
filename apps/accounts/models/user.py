from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    BooleanField,
    CharField,
    EmailField,
    ForeignKey,
    PROTECT,
    DateField,
)

from apps.accounts.managers import UserManager
from apps.core.models import BaseModelMixin


class User(AbstractBaseUser, BaseModelMixin, PermissionsMixin):
    name = CharField(verbose_name="nome completo", max_length=255)
    email = EmailField(verbose_name="endereço de e-mail", unique=True)
    document = CharField(verbose_name="CPF/CNPJ", max_length=18, blank=True, null=True)
    phone = CharField(verbose_name="telefone", max_length=15, blank=True, null=True)
    address = ForeignKey(
        "core.Address",
        verbose_name="endereço",
        on_delete=PROTECT,
        blank=True,
        null=True,
        related_name="user_address",
    )
    birth_date = DateField(verbose_name="data de nascimento", blank=True, null=True)
    # PERMISSIONAMENTO
    is_staff = BooleanField(verbose_name="Pode acessar o painel", default=True)
    is_active = BooleanField(verbose_name="ativo", default=True)

    groups = None
    user_permissions = None

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["name", "-created_at"]

    def __str__(self):
        return self.name
