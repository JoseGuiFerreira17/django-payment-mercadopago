from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
    Serializer,
)

from apps.accounts.models import User
from apps.core.api.serializers import AddressSerializer
from apps.core.models import Address


class UserReadSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ["password"]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
            "is_superuser": {"read_only": True},
        }


class UserDetailSerializer(ModelSerializer):
    address = AddressSerializer(required=False)

    class Meta:
        model = User
        exclude = ["password"]

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        if address_data:
            if instance.address:
                for key, value in address_data.items():
                    setattr(instance.address, key, value)
                instance.address.save()
            else:
                address = Address.objects.create(**address_data)
                validated_data["address"] = address
        return super().update(instance, validated_data)


class UserCreateSerializer(ModelSerializer):
    password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
            "is_superuser": {"read_only": True},
        }

    def validate(self, data):
        if data["password"] != data.pop("confirm_password"):
            raise ValidationError("As senhas não conferem")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ["password"]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
            "name": {"required": False},
            "email": {"required": False},
        }


class UserUpdatePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True)
    password_confirmation = CharField(write_only=True)
    last_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["password", "password_confirmation", "last_password"]

    def validate(self, data):
        user = self.instance
        if not user.check_password(data.pop("last_password")):
            raise ValidationError("Senha atual incorreta")

        if data.get("password") != data.pop("password_confirmation"):
            raise ValidationError("As senhas não conferem")
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
