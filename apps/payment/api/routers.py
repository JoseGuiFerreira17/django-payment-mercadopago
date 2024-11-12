from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.payment.api.viewsets import PaymentViewSet, PaymentMethodViewSet


router = SimpleRouter()

router.register("payment", PaymentViewSet, basename="payment")
router.register("payment-method", PaymentMethodViewSet, basename="payment-method")

urlpatterns = [
    path("", include(router.urls)),
]
