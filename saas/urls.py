from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Schema Definition
schema_view = get_schema_view(
    openapi.Info(
        title="Saas Website Monitor",
        default_version="1.0",
        description="A saas backend application that tracks and monitors website(s) up and down times.",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.monitor.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^afex/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="afex_docs",
        )
    ]
