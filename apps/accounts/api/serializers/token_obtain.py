from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JWTTokenObtainPairSerializer,
)
from apps.accounts.api.serializers.user import UserDetailSerializer


class TokenObtainPairSerializer(JWTTokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        user_data = UserDetailSerializer(user).data
        data.update({"user": user_data})
        return data
