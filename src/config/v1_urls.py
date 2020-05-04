from django.urls import include, path

from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path("docs/", get_swagger_view(title="Example API v1")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
