from django.urls import path, include

from rest_framework.routers import SimpleRouter

from apps.plans.api.viewsets import PlanViewSet, SubscriptionViewSet


router = SimpleRouter()

router.register("plans", PlanViewSet, basename="plans")
router.register("subscriptions", SubscriptionViewSet, basename="subscriptions")

urlpatterns = [
    path("", include(router.urls)),
]
