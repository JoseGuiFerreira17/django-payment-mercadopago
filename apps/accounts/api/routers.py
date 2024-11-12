from django.urls import path, include

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from apps.accounts.api.viewsets import UserViewSet

router = SimpleRouter()

router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/revoke/", TokenBlacklistView.as_view(), name="token_revoke"),
]
