from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.accounts.api.serializers import (
    UserUpdatePasswordSerializer,
    UserReadSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDetailSerializer,
)

from apps.accounts.models import User
from apps.core.api.viewsets import BaseModelViewSet


class UserViewSet(BaseModelViewSet):
    model = User
    serializer_class = UserReadSerializer

    action_serializer_classes = {
        "list": UserReadSerializer,
        "retrieve": UserDetailSerializer,
        "create": UserCreateSerializer,
        "update": UserUpdateSerializer,
        "partial_update": UserUpdateSerializer,
        "me": UserDetailSerializer,
        "password": UserUpdatePasswordSerializer,
    }
    search_fields = ["name", "email", "phone", "birth_date", "document"]

    action_permission_classes = {
        "create": [AllowAny],
    }

    @action(detail=False, methods=["get", "put"])
    def me(self, request, *args, **kwargs):
        user = request.user
        if self.request.method == "GET":
            return Response(self.get_serializer(user).data)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["put"])
    def password(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
