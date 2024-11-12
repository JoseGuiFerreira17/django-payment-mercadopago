from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.core.api.viewsets.content_type import ContentTypeViewSet


router = SimpleRouter()

router.register("content-types", ContentTypeViewSet, basename="content-types")

urlpatterns = [
    path("", include(router.urls)),
]
