from django.urls import path, include

urlpatterns = [
    path("api/v1/auth", include("user.urls")),
]
