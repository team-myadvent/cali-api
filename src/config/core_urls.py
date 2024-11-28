from django.urls import path, include

urlpatterns = [
    path("api/v1/auth", include("user.urls")),
    path("api/v1/profiles", include("profiles.urls")),
]

from config.settings.debug_toolbar import DebugToolbarSetup  # noqa

urlpatterns = DebugToolbarSetup.do_urls(urlpatterns)
