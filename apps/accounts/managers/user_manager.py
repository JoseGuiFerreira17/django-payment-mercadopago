from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DJUserManager

from apps.core.utils import get_request_user


class UserManager(DJUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("O superusuário deve ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("O superusuário deve ter is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def get_or_none(self, *args, **kwargs):
        try:
            return super().get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None

    def all(self):
        user = get_request_user()
        if user:
            if user.is_superuser:
                return super().all()
            return super().filter(office=user.worker_lawyer.office)
        return super().none()
