from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urls_v1 = [
    path("api/v1/", include("apps.urls_v1")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    *urls_v1,
]

admin.site.site_header = "Django Payment"
admin.site.site_title = "Django Payment"
admin.site.index_title = "Administração do Django Payment"
