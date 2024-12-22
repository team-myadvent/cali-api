from django.urls import path

from profiles.views import views


urlpatterns = [
    path(
        "/me",
        views.MyProfileAPI.as_view(),
        name="my-profile",
    ),
    path(
        "/<uuid:profile_id>",
        views.UserProfileDetailAPI.as_view(),
        name="user-profile",
    ),
]
